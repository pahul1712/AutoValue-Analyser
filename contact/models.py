from django.db import models
from django.contrib.auth.models import User


from django.dispatch import receiver
from django.contrib.auth.models import User
from django.db.models.signals import post_save



class Contact(models.Model):
    msg_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=70, default="")
    phone = models.CharField(max_length=70, default="")
    desc = models.CharField(max_length=500, default="")


    def __str__(self):
        return self.name