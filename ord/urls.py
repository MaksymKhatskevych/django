from django.urls import path
from .views import *




urlpatterns = [
    path(r'', contactform, name='order'),
    path(r'thanks/', thanks, name='thanks'),
    # path(r'', DeskListView.as_view(), name='order'),
	
    
]