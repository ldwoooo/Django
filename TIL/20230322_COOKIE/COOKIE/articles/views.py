from django.shortcuts import render, redirect
from .models import Article
from .forms import ArticleForm
# 장고 내장 모듈 사용하는 방법
# from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    articles = Article.objects.all()
    context = {'articles': articles}
    # return render(request, 'articles/index.html', context)
    # 데이터 넣어보기
    response = render(request, 'articles/index.html', context)
    response.set_cookie('message', 'wow')
    return response


def detail(request, pk):
    article = Article.objects.get(pk=pk)
    context = {'article': article}
    return render(request, 'articles/detail.html', context)

# @login_required
def create(request):
    # 함수로 정의해서 사용하는 방법
    # 로그인되지 않은 사용자는 로그인 페이지로 리다이렉션
    # 1. 쿠키에 세션 데이터가 있는가? 없으면 로그인 페이지로 보내기
    # if not request.COOKIES.get('sessionid'):
    #     return redirect('accounts:login')
    # 2. request.user 가 있는가? 없으면 로그인 페이지로 보내기
    # 장고에서는 유저 정보를 request.user 안에 담고있다.
    if not request.user.is_authenticated:
        return redirect('accounts:login')



    if request.method == 'POST':
        form = ArticleForm(request.POST, request.FILES)
        if form.is_valid():
            article = form.save()
            return redirect('articles:detail', article.pk)
    else:
        form = ArticleForm()

    context = {'form': form}
    return render(request, 'articles/create.html', context)


def delete(request, pk):
    article = Article.objects.get(pk=pk)
    article.delete()
    return redirect('articles:index')


def update(request, pk):
    article = Article.objects.get(pk=pk)

    if request.method == 'POST':
        form = ArticleForm(request.POST, request.FILES, instance=article)
        if form.is_valid():
            form.save()
            return redirect('articles:detail', pk=article.pk)
    else:
        form = ArticleForm(instance=article)

    context = {'form': form, 'article': article}
    return render(request, 'articles/update.html', context)
