
from django.urls import path,include
from . import views

urlpatterns = [
    
    path('',views.index,name='home'),
    path('about/',views.about,name='about'),
    path('booking',views.booking,name='booking'),
    path('doctors/', views.doctor_view, name='doctors'),
    path('condact',views.condact,name='condact'),
    path('department',views.department,name='department'),


]