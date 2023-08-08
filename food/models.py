from django.db import models


class Item(models.Model):
    item_name = models.CharField(max_length=100)
    item_description = models.CharField(max_length=225)
    item_price = models.IntegerField()
    item_image = models.URLField(max_length=500,default='https://dha.cafeela.pk/wp-content/uploads/woocommerce-placeholder-433x237.png')
    def __str__(self):
        return self.item_name
    