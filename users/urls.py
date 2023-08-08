from django.urls import path

from . import views

app_name = 'users'


urlpatterns = [
    # /register/ 
    path('',views.register,name='register'),
]