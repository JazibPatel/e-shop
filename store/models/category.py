from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=150)

    @staticmethod
    # this will show all category in html.page and impliment in view.py
    def allcategory():
        return Category.objects.all()

    def __str__(self):
        return self.name
        