from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.views.generic import ListView, CreateView, UpdateView,DeleteView
from django.contrib import messages
from django.urls import reverse_lazy
from .forms import UserRegistrationForm, TalonForm
from .models import *


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

# Talon creation
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