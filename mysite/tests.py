from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
import random
from mysite.models import Car
from mysite.models import Photo
from .forms import UploadModelForm
# Create your views here.
def index(request):
	car = Car.objects.all()
	return render(request, "index.html", locals())
def car(request):
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
	return render(request,"manage.html",locals())
def upload(request):
	photos = Photo.objects.all()  # 查詢所有資料
	form = UploadModelForm()

	if request.method == "POST":
		name = str(request.POST["name"])
		form = UploadModelForm(request.POST, request.FILES)
		if form.is_valid():
			d = Photo(name=name)
			d.save()

			form.save()
			return redirect('/upload/')
	context = {
		'photos': photos,
		'form': form
	}
	return render(request, 'upload.html', context)
def down(request):
	photos = Photo.objects.all()  # 查詢所有資料
	return render(request, 'down.html', locals())