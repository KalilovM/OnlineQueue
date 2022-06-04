
from django.db import models
from django.utils import timezone
import datetime as dt
import time

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
    STATUS = (
        ('Active','Active'),
        ('Passed','Passed'),
        ('Missed','Missed')
    )
    user = models.ForeignKey('accounts.NewUser', on_delete=models.CASCADE)
    number = models.CharField(max_length=100)
    bank = models.ForeignKey(Bank, on_delete=models.CASCADE)
    filial = models.ForeignKey(Filial, on_delete=models.CASCADE)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    arriveTime = models.TimeField(default=dt.time(00, 00), unique=True)
    status = models.CharField(max_length=64, choices=STATUS,default='Active')

    def __str__(self):
        return self.number

    def update_status(self):
        t = dt.datetime.now()
        t1 = t.strftime("%H-%M")
        x = self.arriveTime
        t2 = x.strftime("%H-%M") 
        if t2 <= t1 and self.status == 'Active':
            self.status = 'Missed'
            self.save()

    


    