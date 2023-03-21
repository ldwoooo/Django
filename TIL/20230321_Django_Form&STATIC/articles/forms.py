from django import forms
from .models import Article

# form : 사용자
# Django form 종류는 2가지가 있다.

# 1. Form
#  - 사용자의 입력을 개발자가 직접 구성
#    -> Model의 필드와 관계없이 마음대로 구성할 수 있다.
#  - 장점 : 내 마음대로 원하는 입력을 받을 수 있음
#  - 단점 : DB에 정확히 저장하기 위해서는 models를 완벽하게 파악해야함
#           models.py와 줄일 수 없는 중복 코드가 많이 발생함
class ArticleForm(forms.Form):
    title = forms.CharField(max_length=30)
    # widget: form이 지원하는 기본 기능 외의 추가적인 동작을 원할 때 사용
    content = forms.CharField(widget=forms.Textarea)


# 2. ModelForm
#  - model에 정의된 필드만 입력 받을 수 있음
#  - 장점 : 사용법이 쉽다
#  - 단점 : 내 마음대로 입력을 못 받는다
class ArticleModelForm(forms.ModelForm):
    class Meta:
        model = Article
        # 전체 필드를 받겠다
        fields = '__all__'
        # 원하는 필드만 입력 받겠다.
        # fields = ('title', 'content', 'author', )
        # 주의!!!!
        # 튜플이나 리스트 형태로 작성
        # 반드시 뒤에 콤마로 튜플 표시 해줘야 함!
        # fields = ('title', )

        # 특정 필드를 제외하고 입력 받겠다.
        # 마친가지로 튜플 or 리스트 형대로 작성!!
        # exclude = ('author', )