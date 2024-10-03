from rest_framework.routers import DefaultRouter
from django.urls import path, include
from ..users.views import UserRegistrationView, UserLoginView, AuthenticatedUserView
from ..roles.views import RolesViewSet
from ..courses.views import CourseViewSet
from ..grades.views import GradeViewSet
from ..students.views import StudentViewSet
from ..teachers.views import TeacherViewSet
router = DefaultRouter()

router.register(r'roles', RolesViewSet, basename='roles')
router.register(r'courses', CourseViewSet, basename='course')
router.register(r'grades', GradeViewSet, basename='grade')
router.register(r'students', StudentViewSet, basename='student')
router.register(r'teachers', TeacherViewSet, basename='teacher')


urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name='usuario'),
    path('login/', UserLoginView.as_view(), name='usuario'),
    path('checkAuth/', AuthenticatedUserView.as_view(), name='usuario'),
    path('', include((router.urls)))
]