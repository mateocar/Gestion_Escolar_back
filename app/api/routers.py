from rest_framework.routers import DefaultRouter
from ..users.views import UserRegistrationView


router = DefaultRouter()

router.register(r'register',UserRegistrationView, basename='Usuarios')

urlpatterns = router.urls