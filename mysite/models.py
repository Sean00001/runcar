from django.db import models
from django.contrib import admin
# Create your models here.
from django.utils import timezone

class Car(models.Model):
    #id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100,default='')
    Model = models.CharField(max_length=100,default='')
    Factory_Brand = models.CharField(max_length=100,default='')
    Miles = models.CharField(max_length=100,default='')
    Years = models.CharField(max_length=100,default='')
    Colour = models.CharField(max_length=100,default='')
    Ride = models.CharField(max_length=100,default='')
    Engine = models.CharField(max_length=100,default='')
    def __str__(self):
        return self.name

class Photo(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE)

    image = models.ImageField(upload_to='static/image/', blank=False, null=False)
    upload_date = models.DateField(default=timezone.now)


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Car._meta.fields]


@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Photo._meta.fields]


