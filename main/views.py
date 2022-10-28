from django.shortcuts import render
from django.views.generic import ListView
from .models import News
from django.urls import reverse


class NewsListView(ListView):
	"""Вывод новостей на сайт"""
	def get(self,request):
		news = News.objects.order_by('-published')[:5]

		return render(request,'main/home.html',{'home':news})



class DeskListView(ListView):
    
    def get(self,request):
        template_name = Description.objects.order_by('-published')[:1]
        return render(request, 'ord/order.html', {'value': template_name} )