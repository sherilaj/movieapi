from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Movie(models.Model):
    title = models.CharField(max_length=250)
    lang = models.CharField(max_length=250)
    year = models.DateField(blank= False)
    edited_at = models.DateTimeField(auto_now_add= True)
    def __str__(self):
        return self.title
class Comment(models.Model):
    comment = models.TextField()
    forkey = models.ForeignKey(Movie,on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.user.username}  commented {self.comment} on {self.forkey.title}"
