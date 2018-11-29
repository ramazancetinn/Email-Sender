from django.shortcuts import render, HttpResponseRedirect
from .forms import registration_form
from .models import registration
from django.contrib import messages

# Create your views here.

def registration_create_view(request):

   # form = request.method
    if request.method=="POST":
        form=registration_form(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('index')
    else:
        form = registration_form()

    context = {
    'form': form,
    }

    return render(request, 'registration/reg_create.html', context)

def registration_index_view(request):
    users = registration.objects.all()
    context={
        'users': users
    }
    return render(request, 'registration/reg_index.html', context)