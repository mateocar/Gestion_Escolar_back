pipeline {
  agent any
  environment {
        TF_VAR_azure_username = "${env.azure_username}"
        TF_VAR_azure_password = "${env.azure_password}"
    }
  
  stages {
    stage('Clonar Repo'){
      steps{
        git branch: 'main', url: 'https://github.com/mateocar/Gestion_Escolar_back.git'  
      }
    }
    
    stage('Construir Imagen Docker'){
      steps{
        script {
        def image = docker.build("gestionescolar-backend")
        }
      }
    }

    stage('Terraform Init') {
            steps {
                sh 'terraform init'
            }
        }

    stage('Terraform Validate') {
            steps {
                sh 'terraform validate'
            }
        }
    
    stage('Terraform Import') {
            steps {
                sh 'terraform import azurerm_container_group.gestionescolar /subscriptions/${subscription-id}/resourceGroups/gestion_escolar/providers/Microsoft.ContainerInstance/containerGroups/gestionescolar-container-group || true'
            }
        }
    
    stage('Terraform Plan') {
        steps {
            sh 'terraform plan -out=tfplan'
        }
    }

    stage('Terraform Apply') {
        steps {
            sh 'terraform apply -auto-approve'
        }
    }
  }
}