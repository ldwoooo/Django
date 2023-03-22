from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout

# Create your views here.
def login(request):

    # 2. 로그인(세션 생성) -> POST
    if request.method == 'POST':
        # 1. form 으로 데이터를 받아줌
        form = AuthenticationForm(request, request.POST)
        # 2. 유효성 검사
        if form.is_valid():
            # 3. 로그인
            auth_login(request, form.get_user())
            # 4. index 화면으로 리다이렉션
            return redirect('articles:index')

            

    # 1. 로그인 화면을 보여줘야 함 -> GET
    else:
        form = AuthenticationForm()
        context = {
            'form': form,
        }
        return render(request, 'accounts/login.html', context)
    
def logout(request):
    # sessionid, 로그인 정보 ... 삭제해야할 요청받은 모든 내용을 삭제한다.
    auth_logout(request)
    return redirect('articles:index')
