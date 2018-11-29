from django import forms
from .models import registration

class registration_form(forms.ModelForm):

    class Meta:
        model = registration
        fields =[
            'first_name',
            'last_name',
            'mail_address',
        ]
