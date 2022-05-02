from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import *

class UserRegistrationForm(UserCreationForm):
    first_name = forms.CharField(max_length=101)
    last_name = forms.CharField(max_length=101)
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']


class TalonForm(forms.ModelForm):
    class Meta:
        model = Talon
        fields = ('number', 'bank', 'filial','user')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['filial'].queryset = Filial.objects.none()

        if 'bank' in self.data:
            try:
                bank_id = int(self.data.get('bank'))
                self.fields['filial'].queryset = Filial.objects.filter(bank_id=bank_id).order_by('name')
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty City queryset
        elif self.instance.pk:
            self.fields['filial'].queryset = self.instance.bank.filial_set.order_by('name')