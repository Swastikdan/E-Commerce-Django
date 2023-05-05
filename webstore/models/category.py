# The Category class defines a model for categories with a name field and a static method to retrieve
# all categories.
from django.db import models

class Category(models.Model):
    name= models.CharField(max_length=50)

    @staticmethod
    def get_all_categories():
        return Category.objects.all()

    def __str__(self):
        return self.name
