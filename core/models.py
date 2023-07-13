from django.db import models


class Kit(models.Model):
    class Meta:
        verbose_name = 'Kit'
        verbose_name_plural = 'Kits'
        db_table = 'kit'

    identification = models.CharField('Identificação kit',max_length=400)
    code = models.CharField(max_length=20)
    price = models.DecimalField(max_digits=15, decimal_places=2)
    roof = models.CharField(max_length=30)
    connection =  models.CharField(max_length=20)

    def __str__(self):
        pass


class Module(models.Model):
    amount = models.IntegerField()
    model = models.CharField(30)
    unit_Wp_power = models.IntegerField()
    max_overload = models.IntegerField()
    kWp = models.DecimalField()

class Inverter(models.Model):
    pass

class Cable(models.Model):
    pass