from django.contrib import admin

from .models import *

# Register your models here.


admin.site.register(Category)
admin.site.register(Item)
admin.site.register(Size)
admin.site.register(ItemPrice)
admin.site.register(Topping)
admin.site.register(Order)
admin.site.register(Cart)