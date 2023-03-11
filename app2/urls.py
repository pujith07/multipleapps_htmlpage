from django.urls import path
from app2.views import *

app_name='something'

urlpatterns=[
    path('g/',g,name='g')
]