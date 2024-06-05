from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class Contact(models.Model):
    created = models.DateTimeField(auto_now=True)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=25)
    email = models.EmailField(blank=True, null=True)
    phone_number = PhoneNumberField(blank=True, null=True)

