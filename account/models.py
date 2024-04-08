from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Profile(models.Model):
    gender_choices = (('Male', 'Male'), ('Female', 'Female'))

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    bio = models.TextField(blank=True)
    facebook = models.URLField(blank=True)
    twitter = models.URLField(blank=True)
    instagram = models.URLField(blank=True)
    gender = models.CharField(choices=gender_choices, default='Male', max_length=20)
    date_of_birth = models.DateField(null=True, blank=True)
    profile_picture = models.ImageField(upload_to='users/pictures', blank=True)

    def __str__(self):
        return f'Profile of {self.user.username}'
