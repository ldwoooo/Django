from django.shortcuts import render, redirect
from .models import Article

# Create your views here.
def index(request):
    articles = Article.objects.all()
    context = {
        'articles' : articles,
    }

    return render(request, 'articles/index.html', context)


def create(request):
    if request.method == "POST":
        
        # 저장코드 작성
        title = request.POST.get('title')
        content = request.POST.get('content')

        article = Article(title=title, content=content)
        article.save()

        return redirect('articles:index')

    else:
        return render(request, 'articles/create.html')
    
def detail(request, pk):
    article = Article.objects.get(pk=pk)
    # 삭제
    if request.method == "POST":
        article.delete()
        return redirect('articles:index')
    # 조회
    elif request.method == 'GET':
        context = {
            'article': article,
        }
        return render(request, 'articles/detail.html', context)
    

def update(request, pk):
    article = Article.objects.get(pk=pk)
    # 수정
    if request.method == "POST":
        article.title = request.POST.get('title')
        article.content = request.POST.get('content')
        article.save()
        return redirect('articles:detail', pk)
    # 수정화면
    elif request.method == 'GET':
        context = {
            'article': article,
        }
        return render(request, 'articles/update.html', context)
