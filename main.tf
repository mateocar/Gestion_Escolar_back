terraform {
  required_providers {
    azurerm = {
      source  = "hashicorp/azurerm"
      version = "~> 3.0.2"
    }
  }

  required_version = ">= 1.1.0"
}

variable "azure_username" {
  type = string
}

variable "azure_password" {
  type = string
}

provider "azurerm" {
  features {}
}

resource "null_resource" "az_login" {
  provisioner "local-exec" {
    command = <<EOT
      az login --username "${var.azure_username}" --password "${var.azure_password}"
    EOT
  }
}

data "azurerm_resource_group" "existing" {
  name     = "gestion_escolar"
}

data "azurerm_container_registry" "existing" {
  name                = "miACRuniversidad"
  resource_group_name = data.azurerm_resource_group.existing.name
}

resource "null_resource" "docker_push" {
  provisioner "local-exec" {
    command = <<EOT
      
      az acr login --name ${data.azurerm_container_registry.existing.name}
      docker tag gestionescolar-backend:latest ${data.azurerm_container_registry.existing.login_server}/gestionescolar-backend:latest
      docker push ${data.azurerm_container_registry.existing.login_server}/gestionescolar-backend:latest
    EOT
  }

  depends_on = [data.azurerm_container_registry.existing]
}

resource "azurerm_container_group" "gestionescolar" {
  name                = "gestionescolar-container-group"
  location            = data.azurerm_resource_group.existing.location
  resource_group_name = data.azurerm_resource_group.existing.name
  os_type             = "Linux"

  container {
    name   = "gestionescolar-backend-container"
    image  = "${data.azurerm_container_registry.existing.login_server}/gestionescolar-backend:latest"
    cpu    = "0.5"
    memory = "1.5"

    ports {
      port     = 8000
      protocol = "TCP"
    }
  }

  image_registry_credential {
      server   = data.azurerm_container_registry.existing.login_server
      username = data.azurerm_container_registry.existing.admin_username
      password = data.azurerm_container_registry.existing.admin_password
  }

  depends_on = [null_resource.docker_push,data.azurerm_container_registry.existing]
}
