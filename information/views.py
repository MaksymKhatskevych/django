from django.shortcuts import render
from django.views.generic import ListView
from .models import Information



class NewsListView(ListView):
	"""Вывод новостей на сайт"""
	def get(self,request):
		
		informations = Information.objects.all()
		return render(request,'information/info.html',{'informations':informations})




# Create your views here.
