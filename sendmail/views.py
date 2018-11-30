from django.shortcuts import render
from .forms import send_mail_from
from registration.models import registration
from .models import send_mail

# Create your views here.

def mail_create(request):

    if request.method == 'POST':
        users_mail = registration.objects.values_list('mail_address', 'mail_address')
        users_mail_tuple = tuple(users_mail)
        form = send_mail_from()
        form.fields['mail_list'].choices = [x for x in users_mail_tuple]
        subject_get = request.POST.get('subject')
        message_get = request.POST.get('message')
        recipient_list_get = request.POST.getlist('mail_list')
        status_get = 'NEW'

        dataT=send_mail()
        dataT.subject=subject_get
        dataT.recipient_list=','.join(recipient_list_get)
        dataT.message=message_get
        dataT.status=status_get

        dataT.save()


    else:
        users_mail = registration.objects.values_list('mail_address', 'mail_address')
        users_mail_tuple = tuple(users_mail)
        form = send_mail_from()
        form.fields['mail_list'].choices = [x for x in users_mail_tuple]

    context = {
       'form': form,
        }
    return render(request, 'send_mail/send_create.html', context)