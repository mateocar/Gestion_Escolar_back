from rest_framework.routers import DefaultRouter
from ..users.views import UserRegistrationView


router = DefaultRouter()

router.register(r'users',UserRegistrationView, basename='Usuarios')

urlpatterns = router.urls