from django.shortcuts import render, redirect
from board.models import Post, Comment
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.core.files.storage import default_storage
import uuid
# Create your views here.

def board(request):
    # 게시글 리스트
    if request.method =='GET':
        # 페이지 번호를 파라미터로 받아오며, 기본 값은 1로 설정
        page = request.GET.get('page', 1)
        search_text = request.GET.get('search_text', "")
        # 모든 게시글을 가져온 후, 날짜로 정렬함.
        # i는 대소문자 가리지않고 검색
        post_set = Post.objects.filter(title__icontains=search_text).order_by('-reg_date')
        # 한 페이지당 6개의 게시글을 가져온다.
        paginator = Paginator(post_set, 6)
        # post_set으로 전달함.
        post_set = paginator.get_page(page)

        # print(post_set)
        context = {
            "search_text": search_text,
            "post_set":post_set
        }

        return render(request, 'page/index.html', context = context)

# 로그인 여부 확인. 로그인 안되었을 경우 로그인 페이지로 이동
@login_required(login_url='signin')
def post_write(request):
    # 요청메소드가 GET일 경우
    if request.method == 'GET':
        return render(request, "page/post_write.html")
    
    # 요청메소드가 POST일 경우
    if request.method =='POST':
        title = request.POST['title']
        content = request.POST['content']
        image = request.FILES.get('image', None)
        img_url = ''
        # 만약 이미지가 있을 경우
        if image:
            # uuid를 통한 파일 이름 생성
            img_name = uuid.uuid4()
            ext = image.name.split('.')[-1]

            # (경로, 파일) - 앞서 추가한 upload폴더에 저장
            default_storage.save(f'{img_name}.{ext}', image)
            # 파일 이름
            img_url = f'{img_name}.{ext}'

        # Post 테이블에 저장
        Post(
            user = request.user,
            title=title,
            content=content,
            img_url = img_url
        ).save()

        # 게시글 저장 후 메인 게시판으로 리다이렉트
        return redirect('board')

def post_detail(request, post_id):
    # Get Method일 경우 id 값이 일치하는 게시글을 반환한다.
    if request.method == 'GET':
        post = Post.objects.get(id = post_id)
        context = {
            'post': post
        }
        return render(request, 'page/post_detail.html', context = context)
    
    # 댓글 추가 기능(Post메소드)
    if request.method == 'POST':
        # POST메소드의 content값을 받아와서 comment에 저장함.
        content = request.POST['content']
        Comment(
            post_id = post_id,
            content = content
        ).save()

        # 게시판 상세페이지로 리다이렉트하며, 같이 온 post_id 게시글로 리턴함.
        return redirect('post_detail', post_id)