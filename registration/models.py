from django.db import models

# Create your models here.

class registration(models.Model):
    first_name = models.CharField(max_length=80, verbose_name='First Name')
    last_name = models.CharField(max_length=80, verbose_name='Last Name')
    mail_address = models.EmailField(max_length=200, verbose_name='E-mail Address',unique=True)

    def __str__(self):
        return self.mail_address