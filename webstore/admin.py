'''

This is a Django admin configuration file that registers models for Products, Category, Customer,
and Order with customized display options.

This code registers the Products, Category, Customer, and Order models with the Django admin site. It defines two custom admin classes, AdminProduct and CategoryAdmin, that inherit from Django's admin.ModelAdmin class. These custom classes customize the display of the Products and Category models in the admin panel by specifying the fields to be displayed in the list view (list_display attribute). The AdminProduct class displays the name, price, and category fields, while the CategoryAdmin class displays the name field.

'''
from django.contrib import admin
from .models.product import Products
from .models.category import Category
from .models.customer import Customer
from .models.orders import Order
from .models.contact import Contact

# AdminProduct class, inherits from Django's admin.ModelAdmin class
# Customizes the display of the Product model in the admin panel
class AdminProduct(admin.ModelAdmin):
    list_display = ['name', 'price', 'category']

# CategoryAdmin class, inherits from Django's admin.ModelAdmin class
# Customizes the display of the Category model in the admin panel
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']

# Register the models with the admin site
# Use custom admin classes for Products and Category models
admin.site.register(Products, AdminProduct)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Customer)
admin.site.register(Order)
admin.site.register(Contact)
    

