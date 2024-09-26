from rest_framework.routers import DefaultRouter
from django.urls import path
from ..users.views import UserRegistrationView, UserLoginView, AuthenticatedUserView


# router = DefaultRouter()

# router.register(r'register',UserRegistrationView.as_view(), basename='usuario')

urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name='usuario'),
    path('login/', UserLoginView.as_view(), name='usuario'),
    path('checkAuth/', AuthenticatedUserView.as_view(), name='usuario'),

]