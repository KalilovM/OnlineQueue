from django.db import models
from django.utils import timezone
import datetime as dt

# Create your models here.
class Bank(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Filial(models.Model):
    name = models.CharField(max_length=100)
    bank = models.ForeignKey(Bank, on_delete=models.CASCADE)
    def __str__(self):
        return self.name

class Service(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Talon(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    number = models.CharField(max_length=100)
    bank = models.ForeignKey(Bank, on_delete=models.CASCADE)
    filial = models.ForeignKey(Filial, on_delete=models.CASCADE)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    arriveTime = models.TimeField(default=dt.time(00, 00))
    def __str__(self):
        return self.number