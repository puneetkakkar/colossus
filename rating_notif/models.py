from django.db import models
from django.contrib.auth.models import User
from project.models import project
import datetime
# Create your models here.
class project_like(models.Model):
    class Meta:
        unique_together = (('user', 'project'),)
    user = models.ForeignKey(User)
    project = models.ForeignKey(project)
    date_time = models.DateTimeField(auto_now_add=True,null=True)