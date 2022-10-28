from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.inblog, name='blog-inblog'),
    path('<int:article_id>/', views.detail, name='detail'),
    path('<int:article_id>/leave_comment/', views.leave_comment, name='leave_comment'),
]
