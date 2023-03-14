from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime


# Create your views here.
def index(request):
    return HttpResponse("<h1>LEEDONGWOO</h1>")


def templates(request):
    # return render(request, '(모든앱/templates/)index.html')
    # 모든앱/templates/이 생략되어 있음.
    # 만약 secondapp/templates/index 가 중복되어져 있으면 원하는 결과가 아니니, firstapp으로 묶어준다
    return render(request, 'index.html')


def templates2(request):
    # 변수를 만들고
    name = '이동우'
    # template 로 전달 할 수 있다.
    #                                             마지막에 딕셔너리 형태로 전달
    return render(request, 'firstapp/first.html', {'name' : name})

def templates3(request):
    name = '이동우'
    job = '호랑이'
    menus = ['햄버거', '피자', '치킨']
    title = 'mY nAME Is doNGwoO'
    
    # 일반적으로 변수를 넘길 때 사용하는 방법
    context = {
        'name' : name,
        'job' : job,
        'menus' : menus,
        'title' : title
    }

    return render(request, 'firstapp/first.html', context)


def hw(request):
    menus = ['햄버거', '피자', '치킨']
    today = datetime.now()
    context = {

        'menus' : menus,
        'today' : today,

    }
    
    return render(request, 'firstapp/hw.html', context)
