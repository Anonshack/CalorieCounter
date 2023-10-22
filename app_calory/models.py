from django.db import models


# Create your models here.
class Products(models.Model):
    product_name = models.CharField(max_length=255, verbose_name='Food name')
    product_amount = models.IntegerField(verbose_name='Food amount (100)')
    measures = {
        ('gramm', 'gramm'),
        ('liter', 'liter'),
        ('cup', 'cup'),
        ('spoon', 'spoon'),
        ('piece', 'piece'),
    }
    product_measure = models.CharField(max_length=25, verbose_name='Measure', choices=measures)
    product_calory = models.IntegerField(verbose_name='Product calory')
    product_fat = models.IntegerField(verbose_name='Product fat')
    product_protein = models.IntegerField(verbose_name='Product protein')
    product_carbs = models.IntegerField(verbose_name='Product carbs')
    product_fiber = models.IntegerField(verbose_name='Product fiber')
    product_sugar = models.IntegerField(verbose_name='Product sugar')

    def __str__(self):
        return self.product_name

    class Meta:
        db_table = 'products'