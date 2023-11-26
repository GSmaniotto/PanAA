from django.urls import path
from PanApp import views

urlpatterns = [
    path('', views.index, name='index'),

]
