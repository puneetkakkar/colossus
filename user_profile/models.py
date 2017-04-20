from django.db import models
import datetime
from django.contrib.auth.models import User
from project.models import project


class following_project(models.Model):

    class Meta:
        unique_together = (('user', 'project'),)
    user = models.ForeignKey(User)
    project = models.ForeignKey(project,related_name='project')
    date_time = models.DateTimeField(auto_now_add=True,null=True)

    def __str__(self):
        return 'Follower of : ' + self.user.first_name    

class following_user(models.Model):
    class Meta:
        unique_together = (('user', 'follower'),)
    user = models.ForeignKey(User)
    follower = models.ForeignKey(User,related_name='follower')
    date_time = models.DateTimeField(auto_now_add=True,null=True)

    def __str__(self):
        return 'Follower of : ' + self.user.first_name    

class Photo(models.Model):
    file = models.ImageField()
    description = models.CharField(max_length=255, blank=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = 'photo'
        verbose_name_plural = 'photos'

# def following_stream:

# def following_sub_stream:






