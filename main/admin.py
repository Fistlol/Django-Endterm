from django.contrib import admin
from main.models import Product, Sub_category, Category, Appeal, Profile

# Register your models here.

admin.site.register(Product)
admin.site.register(Sub_category)
admin.site.register(Category)
admin.site.register(Appeal)
admin.site.register(Profile)