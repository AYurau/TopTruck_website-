from django.contrib import admin

# Register your models here.
from main.models import CategorySale, ForSale

admin.site.register(CategorySale)
admin.site.register(ForSale)