from django.urls import path

from .import views

urlpatterns=[
    path('', views.index, name='index'),
    path('Sign_up', views.Sign_up, name='Sign_up'),
    path('Log_in', views.Log_in, name='Log_in'),
    path('Log_out', views.Log_out, name='Log_out'),
    # path('todo', views.todo, name='todo'),
    path('Contact', views.Contact, name='Contact'),
]