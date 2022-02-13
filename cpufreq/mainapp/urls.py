from django.urls import path

from mainapp.views import *

urlpatterns = [
    path('', index, name='main'),
    path('graph/', graph, name='graph'),

]