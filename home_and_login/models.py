from django.db import models
from django.contrib.auth.models import User

#additional user details

class user_details(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    full_name = models.CharField(max_length=50)
    profile_link = models.URLField(default='/welcome_user')
    dob = models.DateField(null=True)
    #add for academic detail
    intro = models.CharField(max_length=200,null=True)
    photo_link = models.URLField(default='/static/images/anonymous-male.png')
    followers_total = models.IntegerField(default=0)
    following_total = models.IntegerField(default=0)
    projects_total = models.IntegerField(default=0)
    
    def __str__(self):
        return 'User_details: ' + self.full_name
