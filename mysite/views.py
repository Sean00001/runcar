from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
import random
from mysite.models import Car
from mysite.models import Photo
from .forms import UploadModelForm
from django.core.files.base import ContentFile
# Create your views here.
from django.contrib import auth
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate

def index(request):
	data = list()
	cars = Car.objects.all()
	for car in cars:
		item = dict()
		item['name'] = car.name
		item['Model'] = car.Model
		item['Factory_Brand'] = car.Factory_Brand
		item['Miles'] = car.Miles
		item['Years'] = car.Years
		item['Colour'] = car.Colour
		item['Ride'] = car.Ride
		item['Engine'] = car.Engine
		photos = Photo.objects.filter(car=car)
		images = list()
		for photo in photos:
			images.append(photo.image)
		data.append([item,images])
	return render(request, "index.html", locals())
def car(request):
	years = range(1997, 2021)
	engines = [ "汽油", "柴油", "油電"]
	number = [ "四人", "五人", "七人"]
	if request.method == "POST":
		print("Model=", str(request.POST["Model"]))
		print("Factory_Brand=", str(request.POST["Factory_Brand"]))
		print("Miles=", str(request.POST["Miles"]))
		print("Years=",str(request.POST["Years"]))
		print("Colour=", str(request.POST["Colour"]))
		name = str(request.POST["name"])
		Model = str(request.POST["Model"])
		Factory_Brand = str(request.POST["Factory_Brand"])
		Miles = str(request.POST["Miles"])
		Years = str(request.POST["Years"])
		Colour = str(request.POST["Colour"])
		Ride = str(request.POST["Ride"])
		Engine = str(request.POST["Engine"])

		d = Car(Model=Model,Factory_Brand=Factory_Brand,Miles=Miles,Years=Years,Colour=Colour,Ride=Ride,Engine=Engine,name=name)
		d.save()
		return redirect('/upload/')

	return render(request,"car.html",locals())
def upload(request):
	# car = Car.objects.all()
	photos = Photo.objects.all()  # 查詢所有資料
	car = Car.objects.all()
	form = UploadModelForm()
	if request.method == "POST":
		form = UploadModelForm(request.POST, request.FILES)
		if form.is_valid():
			form.save()
			return redirect('/upload/')             #redirect裡面放url參數，目的是要跳轉到這個網址去
	context = {
		'photos': photos,
		'form': form,
		'car': car
	}
	# return render(request, 'upload.html', {'context': context, 'car':car})
	return render(request, 'upload.html', context)

def down(request):
	photos = Photo.objects.all()  # 查詢所有資料
	return render(request, 'down.html', locals())
def contact(request):
	car = Car.objects.all()
	photo = Photo.objects.all()
	return render(request, 'contact.html', locals())
def log_in(request):
	username = "admin"
	password = 12345
	if request.method == "POST":
		name = str(request.POST["username"])
		password = str(request.POST["password"])
		if (username==name and password==password):
			return render(request, 'manage.html', locals())
		else:
			return render(request, 'log_in.html', locals())
	return render(request, 'log_in.html', locals())
def manage(request):
	car = Car.objects.all()
	photo = Photo.objects.all()
	return render(request, 'manage.html', locals())

def delete(request):
	car = Car.objects.all()
	if request.method == "POST":
		# name = request.GET.get('name')
		name = str(request.POST["name"])

		# duser = Car.objects.get(name=name)
		# duser.delete()
		print(name)
		Car.objects.filter(name=name).delete()
		# return HttpResponse(duser.cname)
	return render(request, 'delete.html', locals())