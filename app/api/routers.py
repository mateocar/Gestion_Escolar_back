from rest_framework.routers import DefaultRouter
from django.urls import path
from ..users.views import UserRegistrationView


# router = DefaultRouter()

# router.register(r'register',UserRegistrationView.as_view(), basename='usuario')

urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name='usuario')
]