from django.db import models
from django.db.models.base import Model
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE 
from django.utils.timezone import now

# Create your models here.
class Post(models.Model):
    sno=models.AutoField(primary_key=True)
    title=models.CharField(max_length=255)
    content=models.TextField()
    author=models.CharField(max_length=14)
    slug=models.CharField(max_length=130)
    timestamp=models.DateTimeField(blank=True)

    def __str__(self):
        return self.title +' by' + self.author


# For Comments
class BlogComment(models.Model):
    sno=models.AutoField(primary_key=True)
    comment=models.TextField()
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    post=models.ForeignKey(Post,on_delete=models.CASCADE)
    parent=models.ForeignKey('BlogComment',on_delete=models.CASCADE,null=True)
    timestamp=models.DateTimeField(default=now)
    
    def __str__(self) :
        return self.comment[0:13] +'....' + "by " + self.user.first_name