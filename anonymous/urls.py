"""anonymous URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from board.views import board, post_write, post_detail
from user.views import signin, signup, signout
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path("",  board, name = "board"),
    path("user/signin", signin, name = 'signin'),
    path("user/signup", signup, name = 'signup'),
    path("user/signout", signout, name = 'signout'),
    path("post/write", post_write, name = 'post_write'),
    path("post/<int:post_id>", post_detail, name = 'post_detail'),
]

# 시스템의 디버그가 True인경우(개발중), 문서 경로를 static으로 추가함.
if settings.DEBUG:
    urlpatterns += static('upload', document_root=settings.MEDIA_ROOT)