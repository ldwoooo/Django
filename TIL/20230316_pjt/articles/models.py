from django.db import models

# Create your models here.

class Article(models.Model):
    # 글자수가 정해져 있는 필드
    title = models.CharField(max_length=20)
    # 글자수가 정해져 있지 않은 필드
    content = models.TextField()

    def __str__(self):
        return f'{self.title} {self.content}'