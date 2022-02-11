from django.db import models

# Create your models here.
class Course(models.Model):
    sno=models.AutoField(primary_key=True)
    title=models.TextField(default="")
    timestamp=models.DateTimeField()
    photo = models.ImageField(upload_to="tutorials/course",default="")
    slug=models.CharField(max_length=130,default="")

    def __str__(self):
        return self.title 

class Topics(models.Model):
    sno=models.AutoField(primary_key=True)
    title=models.CharField(max_length=500)
    content=models.TextField()
    course=models.ForeignKey(Course,on_delete=models.CASCADE)
    timestamp=models.DateTimeField()
    slug=models.CharField(max_length=130)
    photo = models.ImageField(upload_to="tutorials/topics",default="")
    def __str__(self):
        return self.title