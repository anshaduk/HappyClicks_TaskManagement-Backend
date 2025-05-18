from django.urls import path,include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView
from . import views


router = DefaultRouter()
router.register(r'tasks',views.TaskViewSet,basename='task')


urlpatterns = [
    path('',include(router.urls)),
    path('register/',views.register_user,name='register'),
    path('token/',TokenObtainPairView.as_view(),name='token_obtain_pair'),
    path('token/refresh/',TokenRefreshView.as_view(),name='token_refresh'),
    path('task-stats/',views.task_stats,name='task_stats'),
]