from django.urls import path

from . import views

app_name = 'food'

urlpatterns = [
    # /food/
    path('', views.index, name='index'),
    
    # /food/1/ 
    path('<int:pk>/',views.item_detail,name='item_detail'),
    path('add/',views.add_item,name='add_item'),
    path('edit/<int:pk>/',views.edit_item,name='edit_item'),
    path('delete/<int:pk>/',views.delete_item,name='delete_item'),
]