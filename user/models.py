from django.db import models
from django.contrib.auth.models import AbstractUser, AbstractBaseUser
# AbstractUser
# Django의 기본 유저 모델
# 각종 필드, 함수(유저 생성, 유저 인증 등)이 포함되어 있음.)
class User(AbstractUser):
    nickname = models.CharField(max_length = 30)

    class Meta:
        db_table='user'

#AbstractBaseUser
# django의 최소 유저 모델
# 필드: 비밀번호, 마지막 로그인, 활성 여부 3가지만 존재
# 따라서 로그인 시 필요한 필드 커스텀 가능함.