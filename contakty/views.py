from django.shortcuts import render
from django.views.generic import ListView
from .models import Contact



class NewsListView(ListView):
	"""Вывод новостей на сайт"""
	def get(self,request):
		
		contacts = Contact.objects.all()
		return render(request,'contakty/contakty.html',{'contacts':contacts})

# Create your views here.
