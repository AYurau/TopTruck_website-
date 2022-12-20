from django.db import models


# Create your models here.
class CategorySale(models.Model):
    name = models.CharField(max_length=64, verbose_name='Category')


    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name


class ForSale(models.Model):
    title = models.CharField(max_length=255, verbose_name='Title')
    category = models.ForeignKey(CategorySale, on_delete=models.CASCADE, verbose_name='Category')
    description = models.CharField(max_length=255, verbose_name='Description')
    options = models.CharField(max_length=255, verbose_name='Options')
    price = models.FloatField(verbose_name='Цена')
    cover = models.ImageField(upload_to='static/img/')

    class Meta:
        verbose_name = 'Machine'
        verbose_name_plural = 'Machines'

    def __str__(self):
        return self.title
