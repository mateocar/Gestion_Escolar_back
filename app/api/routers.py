from rest_framework.routers import DefaultRouter
from django.urls import path, include
from ..users.views import UserRegistrationView, UserLoginView, AuthenticatedUserView
from ..roles.views import RolesViewSet

router = DefaultRouter()

router.register(r'roles', RolesViewSet, basename='roles')

urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name='usuario'),
    path('login/', UserLoginView.as_view(), name='usuario'),
    path('checkAuth/', AuthenticatedUserView.as_view(), name='usuario'),
    path('', include((router.urls)))
]