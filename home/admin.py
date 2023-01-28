from django.contrib import admin
from .models import SellProperty,Customer, Buyer, EmiRequest, Category

# Register your models here.

admin.site.register(SellProperty)
admin.site.register(Customer)
admin.site.register(Buyer)
admin.site.register(EmiRequest)
admin.site.register(Category)
