from django.db import models

# Create your models here.
class Article(models.Model):    # 외워주기
    # textfield-> 긴 거 , charfield-> 짧은 거
    # models. <- 얘는 장고에서 정해놓은 거기 때문에 외워야함
    title = models.CharField(max_length=20)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)