from django.shortcuts import render, redirect
from .models import Article

def throw(request):
    return render(request, 'articles/throw.html')

def catch(request):
    message = request.POST.get('data')
    context = {
        'message':message
    }
    return render(request, 'articles/catch.html', context)

def articles(request):
    # 전체조회
    articles = Article.objects.all()
    context = {
        'articles' : articles,
    }
    return render(request, 'articles/articles.html', context)

def create(request):

    return render(request, 'articles/create.html')

# 실제로 데이터를 DB에 저장
def new(request):
    # 데이터 받아오기
    title = request.POST.get('title')
    content = request.POST.get('content')

    # DB에 저장
    Article.objects.create(title=title, content=content)

    # 생성 후 전체 목록 리스트로 가야함
    return redirect('myapps:articles' )
    # 같은 의미
    # BUT,메모리를 많이 차지 하고 길고 상세주소를 두 개로 다뤄야 하는 등 단점이 많음
    # articles = Article.objects.all()
    # context = {
    #     'articles':articles,
    # }
    # return render(request, 'myapps/articles.html', context)