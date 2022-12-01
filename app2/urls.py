from django.urls import path
from app2.views import *
app_name='nikky'

urlpatterns=[
    path('a2_one/',a2_one,name='a2_one'),
]