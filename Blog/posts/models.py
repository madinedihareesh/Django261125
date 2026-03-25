from django.db import models

# Create your models here
class Post(models.Model):
    post_title = models.CharField(max_length=200)
    post_dis=models.TextField()
    post_Cdate = models.DateField(auto_now=True)
    post_url=models.TextField(default="someurl")

