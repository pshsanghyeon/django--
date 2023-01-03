from django.db import models

# Create your models here.

class Menu(models.Model):
    name = models.CharField(max_length=100, blank=True)
    
    def __str__(self):
        return self.name


class MainMenu(models.Model):
    name = models.CharField(max_length=100)
    content = models.TextField(blank=True)
    price = models.IntegerField(default=0)
    img = models.ImageField(null=True)
    kind = models.ForeignKey(Menu, on_delete=models.CASCADE, null=True)
    
    def __str__(self):
        return self.name

class SideMenu(models.Model):
    name = models.CharField(max_length=100)
    content = models.TextField(blank=True)
    price = models.IntegerField(default=0)
    img = models.ImageField(null=True)
    kind = models.ForeignKey(Menu, on_delete=models.CASCADE, null=True)
    
    
    def __str__(self):
        return self.name

class DrinkMenu(models.Model):
    name = models.CharField(max_length=100)
    content = models.TextField(blank=True)
    price = models.IntegerField(default=0)
    img = models.ImageField(null=True)
    kind = models.ForeignKey(Menu, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name

class SetMenu(models.Model):
    name = models.CharField(max_length=100)
    content = models.TextField(blank=True)
    price = models.IntegerField(default=0)
    img = models.ImageField(null=True)
    kind = models.ForeignKey(Menu, on_delete=models.CASCADE, null=True)
    
    def __str__(self):
        return self.name

class InariMenu(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField(default=0)
    content = models.TextField(blank=True)
    img = models.ImageField(null=True)
    kind = models.ForeignKey(Menu, on_delete=models.CASCADE, null=True)
    
    def __str__(self):
        return self.name

class CoffeeMenu(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField(default=0)
    img = models.ImageField(null=True)
    kind = models.ForeignKey(Menu, on_delete=models.CASCADE, null=True)
    
    def __str__(self):
        return self.name

class BasicMenu(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField(default=0)
    img = models.ImageField(null=True)
    kind = models.ForeignKey(Menu, on_delete=models.CASCADE, null=True)
    
    def __str__(self):
        return self.name
    
    