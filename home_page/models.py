from django.db import models

# Create your models here.

class Category(models.Model):
    category = models.CharField(max_length=150)

    def __str__(self):
        return self.category
    
class Brand(models.Model):
    brand = models.CharField(max_length=150)

    def __str__(self):
        return self.brand
    
class ShopItem(models.Model):
    NameItem = models.CharField(max_length=150)
    ImageItem = models.ImageField(upload_to="images")
    DataItem = models.DateField(auto_now=False)
    PriceItem = models.DecimalField(decimal_places=2, max_digits=1000)
    TagItem = models.CharField(max_length=150)
    category = models.ManyToManyField(Category)
    brand = models.ManyToManyField(Brand)
    available = models.IntegerField(null=True)
    prefer = models.CharField(max_length=150, null=True)
    on_chart = models.CharField(max_length=5, null=True)
    quantity = models.IntegerField(null=True)
    
    def __str__(self):
        return self.NameItem
    

