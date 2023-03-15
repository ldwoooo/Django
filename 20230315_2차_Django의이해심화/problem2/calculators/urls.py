
from django.urls import path
from . import views

urlpatterns = [
    path('', views.start),
    path('<int:number>/<int:number2>/', views.index),
]
