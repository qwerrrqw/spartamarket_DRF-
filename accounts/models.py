from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    nickname = models.CharField(max_length=150, unique=True)  # 필수 입력
    birthday = models.DateField()  # 필수 입력
    gender = models.CharField(max_length=10, blank=True, null=True)  # 선택 입력 (blank=True, null=True)
    PR = models.TextField(blank=True)  # 선택 입력 (자기소개, blank=True로 설정)

    def __str__(self):
        return self.username