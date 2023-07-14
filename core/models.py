from django.db import models


class Kit(models.Model):
    class Meta:
        verbose_name = 'Kit'
        verbose_name_plural = 'Kits'
        db_table = 'kit'

    type_kit = models.CharField(max_length=30)
    identification = models.CharField('Identificação kit',max_length=400)
    code = models.CharField(max_length=20)
    price = models.DecimalField(max_digits=15, decimal_places=2)
    roof = models.CharField(max_length=30)
    connection =  models.CharField(max_length=20)
    
    quantity_modules = models.IntegerField()
    module_model = models.CharField(max_length=30)
    module_unit_Wp_power = models.IntegerField()
    max_overload = models.IntegerField()
    kWp = models.DecimalField(max_digits=10, decimal_places=4)
    module_brand = models.CharField(max_length=30)

    inverter_1_model = models.CharField(max_length=100, null=True)
    inverter_1_quantity = models.IntegerField(null=True)
    inverter_2_model = models.CharField(max_length=100, null=True)
    inverter_2_quantity = models.IntegerField(null=True)
    inverter_brand = models.CharField(max_length=30, null=True)

    amount_of_red_cables = models.IntegerField()
    model_red_cables = models.CharField(max_length=100)
    amount_of_black_cables = models.IntegerField()
    model_black_cables = models.CharField(max_length=100)

    connector_pair_model = models.CharField(max_length=100, null=True)
    quantity_pairs_connector = models.IntegerField(null=True)

    model_stringbox = models.CharField(max_length=100, null=True)
    quantity_stringbox = models.IntegerField(null=True)

    model_structure_1 = models.CharField(max_length=100, null=True)
    quantity_structure_1 = models.IntegerField(null=True)

    model_structure_2 = models.CharField(max_length=100, null=True)
    quantity_structure_2 = models.IntegerField(null=True)

    model_structure_3 = models.CharField(max_length=100, null=True)
    quantity_structure_3 = models.IntegerField(null=True)

    model_structure_4 = models.CharField(max_length=100, null=True)
    quantity_structure_4 = models.IntegerField(null=True)

    model_structure_5 = models.CharField(max_length=100, null=True)
    quantity_structure_5 = models.IntegerField(null=True)

    def __str__(self):
        return str(self.identification)
