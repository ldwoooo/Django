"""firstpjt URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from firstapp import views

urlpatterns = [
    # 127.0.0.1:8000/admin/ 으로 요청을  보냈을 때 보냈을 때 응답한다.
    path('admin/', admin.site.urls),
    # 127.0.0.1:8000/test/ 로 요청을 보냈을 떄 응답한다.
    path('test/', views.index),

    # 'firstapp' : 주소명. html 뒤에 적을 상세주소값. 아무거나 쳐도 된다. 변수명이랑 똑같음
    path('firstapp/', views.templates),
    path('firstapp/first/', views.templates2),
    path('firstapp/third/', views.templates3),
    path('hw/', views.hw)

]
