from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.views.generic import ListView, CreateView, UpdateView,DeleteView
from django.contrib import messages
from django.urls import reverse_lazy
from .forms import UserRegistrationForm, TalonForm
from .models import *
import datetime as dt
import time
from accounts.models import NewUser

user_pk = 0
def get_user_pk(request):
    global user_pk
    user_pk = request.user.pk
    print(user_pk)
    return user_pk

# User creation view
def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f'Your account has been created. You can log in now!')
            return redirect('login')
    else:
        form = UserRegistrationForm()

    context = {'form': form}
    return render(request, 'register.html', context)

def landing(request):
    return render(request, 'landing.html')

def product(request):
    return render(request, 'product.html')

def sectors(request):
    return render(request, 'sectors.html')

def about(request):
    return render(request, 'about.html')
def profile(request):
    return render(request, 'profile.html')

# Talon creation
def home(request):
    act = Talon.objects.filter(status='Active')
    for i in act:
        Talon.update_status(i)
    psd = Talon.objects.filter(status='Passed')
    msd = Talon.objects.filter(status='Missed')

    context = {
        'acts' : act,
        'psds' : psd,
        'msds' : msd,
    }
    return render(request, 'talon_list.html', context)



class TalonListView(ListView):
    model = Talon
    context_object_name = 'ticket'
    template_name = 'talon_list.html'

class TalonCreateView(CreateView):
    model = Talon
    form_class = TalonForm
    template_name = 'talon_form.html'
    success_url = reverse_lazy('talon_changelist')
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class TalonUpdateView(UpdateView):
    model = Talon
    form_class = TalonForm
    template_name = 'talon_form.html'
    success_url = reverse_lazy('talon_changelist')

class TalonDeleteView(DeleteView):
    model = Talon
    template_name = 'talon_confirm_delete.html'
    success_url = reverse_lazy('talon_changelist')

def load_filial(request):
    bank_id = request.GET.get('bank')
    filials = Filial.objects.filter(bank_id=bank_id).order_by('name')
    return render(request, 'filial_dropdown_list_options.html', {'filials': filials})


def UpdateUser(request, pk):
    user = NewUser.objects.get(pk=pk)
    form = UserRegistrationForm(instance=user)
    if request.method == 'POST':
        form = UserRegistrationForm(data = request.POST, files = request.FILES, instance=user)
        if form.is_valid():
            form.save()
            return redirect('talon_changelist')
    context = {
        'form' : form
    }
    return render(request,'user.html', context)


