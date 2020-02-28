from rest_framework.routers import DefaultRouter
from django.urls import path, include

from user import views


router = DefaultRouter()
router.register('users', views.UserViewSet.as_view(), base_name='user-list'),
router.register('login', views.LoginView.as_view(), basename='login'),

url_patterns = [
    path('', include(router.urls)),
    path('account/login/', views.LogoutView.as_view(), name='logout')
]