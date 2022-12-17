from django.urls import path
from . import views
urlpatterns=[
    path('',views.index,name='index'),
    path('schedule',views.schedule_mail,name='mail')
]