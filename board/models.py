from django.db import models
from user.models import User
# Create your models here.
class Post(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    title = models.CharField(max_length =100)
    content = models.TextField()
    reg_date = models.DateTimeField(auto_now_add = True)
    img_url = models.URLField(null = True)
    
    class Meta:
        # 만약 이름을 지정하지 않으면 app_model (ex: board_post)
        db_table = "post"

# FK -> Parents.children_set
# Post.comment_set
class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete = models.CASCADE)
    content = models.TextField()
    reg_date = models.DateTimeField(auto_now_add = True)

    class Meta:
        db_table = 'comment'