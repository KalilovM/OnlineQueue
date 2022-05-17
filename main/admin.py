from django.contrib import admin

# Register your models here.
from .models import *
admin.site.register(Bank)
admin.site.register(Filial)
admin.site.register(Talon)
admin.site.register(Service)