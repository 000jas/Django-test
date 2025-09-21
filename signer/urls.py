from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),                 # Homepage
    path('api/sign/', views.SignMessageView.as_view(), name='sign-message'),
    path('api/verify/', views.VerifyMessageView.as_view(), name='verify-message'),
]
