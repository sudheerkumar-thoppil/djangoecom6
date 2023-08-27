from django.db import models

# Create your models here.
class Product(models.Model):
    item_name=models.CharField(max_length=50)
    item_price=models.FloatField(default=0)
    item_image=models.ImageField(upload_to='media')

    def __str__(self):
        return self.item_name
        