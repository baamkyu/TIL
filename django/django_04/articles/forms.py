from django import forms
from .models import Article

# class ArticleForm(forms.Form):
#     # 사용자한테 받을 것들 (제목, 내용 등)
#     title = forms.CharField(max_length=10)  # models.py에서와는 다르게 max_length가 필수 사항은 아님
#     content = forms.CharField(widget=forms.Textarea)    # models.py에서와는 다르게 textField가 존재하지 않음

#     # 또한 forms.py는 파일 위치에 규약이 없으나 편하게 관리하기 위해 앱폴더 안에 작성

class ArticleForm(forms.ModelForm):     # 안에 뭐가 들어갈지는 장고 공식문서 활용
    title = forms.CharField(
        label='제목', 
        widget=forms.TextInput(
            attrs=
                'class':'my-title',
                'placeholder': 'Enter the title', 
                'maxlength': 10,
        )
    )
    content = forms.CharField(
        label='내용',
        widget=forms.Textarea{
            attrs={
                'class': 'my-content',
                'placeholder': 'Enter the content',
                'rows': 5,
                'cols': 50,
            }
        }
        error_messages={
            'required': 'Please enter your content',
        }
    )
    class Meta:
        model = Article         # 어떤 모델을 기반으로 할지
        fields = '__all__'      # 어떤 모델필드 중 어떤 것을 출력할지
                                # '__all__' : 아티클 모델에서 사용자로부터 입력받는 모든 필드
        # exclude = ('title',)    # 제외시킬 변수는 exclude 사용