from django.db import models
from users.models import User


# Create your models here.
class Post(models.Model):
    title = models.CharField("제목", max_length=20)
    content = models.TextField("내용")
    thumbnail = models.ImageField("썸네일", upload_to='post', blank=True, null=True)

    def __str__(self):
        return self.title

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    content = models.TextField("댓글 내용")

    def __str__(self):
        return f"{self.post.title} - {self.content}"
