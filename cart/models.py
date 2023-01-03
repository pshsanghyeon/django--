from django.db import models
from menu.models import Menu
# Create your models here.

class Cart(models.Model):
    name = models.CharField(max_length=200)
    price = models.IntegerField(default=0)
    num = models.IntegerField(default=0)
    img = models.ImageField(null=True)
    kind = models.ForeignKey(Menu, on_delete=models.CASCADE, null=True)
    
    def __str__(self):
        return f"{self.name}"
    
    
