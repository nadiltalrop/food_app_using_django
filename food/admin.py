from django.contrib import admin
from .models import Item


class ItemAdmin(admin.ModelAdmin):
    list_display = ('id','item_name','item_description',"item_price")
  
admin.site.register(Item, ItemAdmin)