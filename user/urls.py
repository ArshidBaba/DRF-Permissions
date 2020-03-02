from rest_framework.routers import DefaultRouter
from django.urls import path, include

from .views import UserViewSet, LoginView, LogoutView


router = DefaultRouter()
router.register('users', UserViewSet, basename='user-list'),
router.register('login', LoginView, basename='login'),

urlpatterns = [
    # path('', include(router.urls)),
    path('account/login/', LogoutView.as_view(), name='logout')
] 

urlpatterns += router.urls