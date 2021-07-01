from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.name}"
    class Meta:
        verbose_name_plural = "Category"



class Item(models.Model):
    name = models.CharField(max_length=255)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="items")

    def __str__(self):
        return f"{self.name}"
    class Meta:
        verbose_name_plural = "Item"


class Size(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name_plural = "Size"



class ItemPrice(models.Model):
    price = models.FloatField()
    size = models.ForeignKey(Size, on_delete=models.CASCADE, related_name="sizes")
    item = models.ForeignKey(Item, on_delete=models.CASCADE, related_name="prices")

    def __str__(self):
        return f"{self.item} -> {self.price} {self.size}"

    class Meta:
        verbose_name_plural = "ItemPrice"


class Topping(models.Model):
    name = models.CharField(max_length=64)
    items = models.ManyToManyField(Item, blank=True, related_name="toppings")

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name_plural = "Topping"

class Cart(models.Model):
    name = models.CharField(max_length=255)
    quantity = models.IntegerField()
    size = models.CharField(max_length=64)
    price = models.FloatField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="carts") 

    def __str__(self):
        return f"{self.user.username} {self.name} {self.quantity} {self.size} {self.price}"
    class Meta:
        verbose_name_plural = "Cart"

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="orders") 
    items = models.IntegerField()
    total = models.FloatField()
    status = models.BooleanField() 
    def __str__(self):
        return f"{self.user.username} purcahsed {self.items} item(s) ----- {self.total} ----- Status: ----- {self.status} -----"
    class Meta:
        verbose_name_plural = "Order"