from django.db import models

# Create your models here.

class send_mail(models.Model):
    subject = models.CharField(max_length=75, verbose_name='Subject')
    recipient_list = models.CharField(max_length=200, verbose_name='Recipient List')
    message = models.TextField(verbose_name='Message')
    status = models.CharField(max_length=25, default='NEW')

    def __str__(self):
        return self.recipient_list

