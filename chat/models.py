from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username

class ChatGroup(models.Model):
    name = models.CharField(max_length=245)

    def __str__(self):
        return self.name

class UserChatGroup(models.Model):
    user = models.ForeignKey('Profile', on_delete=models.CASCADE)
    group = models.ForeignKey('ChatGroup')

    def __str__(self):
        return self.user.user.username + ' ' + self.group.name

