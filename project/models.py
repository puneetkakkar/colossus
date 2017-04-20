from django.db import models
from django.contrib.auth.models import User
import datetime
from django.forms import ModelForm

class project(models.Model):
    project_type_choices = (
        ('Med', 'Medical'),
        ('Lit', 'Literature'),
    )
    # user = models.OneToOneField(User,on_delete=models.CASCADE)
    user = models.ForeignKey(User)
    title = models.CharField(max_length = 120)
    project_type = models.CharField(
        max_length=200,
        choices=project_type_choices,
        default = 'NO' 
    )
    project_link = models.CharField(max_length=85, default='error.html')
    likes_total = models.IntegerField(default=0)
    comments_total = models.IntegerField(default=0)
    shares_total = models.IntegerField(default=0)
    following_total = models.IntegerField(default=0)
    date_time = models.DateTimeField(auto_now_add=True,null=True)
    description = models.TextField()
    #add achievements

class file_model(models.Model):
    # file_name = models.CharField(max_length=20, null=True)
    file_project_link = models.FileField(upload_to='project_sih/static/user_media', default=True)

class file_modal_form(ModelForm):
    class Meta:
        model = file_model
        fields = '__all__'