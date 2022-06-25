from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField


class Profile(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    name = models.CharField(max_length=25)
    address = models.TextField(blank=True,null=True)
    pincode = models.IntegerField(blank=True,null=True)
    mobile = PhoneNumberField(unique=True)

    def __str__(self):
        return str(self.user) 






