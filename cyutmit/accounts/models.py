from django.db import models
from django.contrib.auth.models import User



class UserProfile(models.Model):
    user = models.OneToOneField(User)
    fullName = models.CharField(max_length=128)
    
    def __str__(self):
        return self.fullName + ' (' + self.user.username + ')'