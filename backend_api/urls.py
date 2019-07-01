from django.urls import path

from backend_api import views

urlpatterns = [
    path('testapiview/', views.TestAPIView.as_view()),
]
