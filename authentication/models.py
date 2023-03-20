from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    
    photo = models.ImageField(upload_to='users_img/', null=True, blank=True)
    
    @property
    def fileURL(self):
        try:
            url = self.photo.url
        except:
            url = ''
        return url