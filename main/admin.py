from django.contrib import admin

# Register your models here.
from main.models import CategorySale, ForSale, Details, DetailCategory

admin.site.register(CategorySale)
admin.site.register(ForSale)
admin.site.register(Details)
admin.site.register(DetailCategory)