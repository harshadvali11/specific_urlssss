from django.urls import path

app_name='app2'

from app2 import views

urlpatterns=[
    path('fun/',views.app2_fun,name='app2_fun'),
]