from django.urls import path, include
from rest_framework.routers import DefaultRouter

from backend_api import views

# Registering ViewSet\
router = DefaultRouter()
router.register('testviewset', views.TestViewSet, base_name='testviewset')
router.register('profile', views.UserProfileViewSet)

urlpatterns = [
    path('testapiview/', views.TestAPIView.as_view()),
    path('login/',views.UserLoginAPIView.as_view()),
    path('', include(router.urls)) # ViewSet
]
