from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'), 
    path('head/', views.head, name='head'),
    path('submit-form/', views.head, name='submit_form'),
    # path('data/', views.data , name="data")
]
