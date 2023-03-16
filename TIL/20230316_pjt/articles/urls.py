from django.urls import path
from . import views

app_name="myapps"
urlpatterns = [
    path('throw/', views.throw, name='throw'),
    path('catch/', views.catch, name='catch'),
    path('articles/', views.articles, name='articles'),
    path('create/', views.create, name='create'),
    path('new/', views.new, name='new'),
]
