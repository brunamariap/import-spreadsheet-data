from django import forms
from .models import Kit
from django.db.models import Count


class KitFilterForm(forms.Form):
    default_option_selected = ('' ,'Selecione uma opção')

    types = Kit.objects.values('type_kit').annotate(total_kits=Count('id'))
    KIT_TIPES_CHOICES = [default_option_selected]
    KIT_TIPES_CHOICES.extend((x['type_kit'], x['type_kit']) for x in types)

    types_inverter_brand = Kit.objects.values(
        'inverter_brand').annotate(total_kits=Count('id'))
    INVERTER_BRAND_CHOICES = [default_option_selected]
    INVERTER_BRAND_CHOICES.extend(
        (x['inverter_brand'], x['inverter_brand']) for x in types_inverter_brand)

    types_module_brand = Kit.objects.values(
        'module_brand').annotate(total_kits=Count('id'))
    MODULE_BRAND_CHOICES = [default_option_selected]
    MODULE_BRAND_CHOICES.extend((x['module_brand'], x['module_brand'])
                            for x in types_module_brand)
    
    types_roof = Kit.objects.values(
        'roof').annotate(total_kits=Count('id'))
    TYPES_ROOF_CHOICES = [default_option_selected]
    TYPES_ROOF_CHOICES.extend((x['roof'], x['roof'])
                            for x in types_roof)
    
    ORDER_BY_CHOICES = [
        default_option_selected,
        ('asc', 'Menor preço'),
        ('desc', 'Maior preço'),
    ]

    type_kit = forms.ChoiceField(label='Tipo do kit', choices=KIT_TIPES_CHOICES, required=False, widget=forms.Select(
        attrs={
            'class': "text-gray rounded-lg px-4",
        }))
    inverter_brand = forms.ChoiceField(label='Marca do inversor', choices=INVERTER_BRAND_CHOICES, required=False, widget=forms.Select(
        attrs={
            'class': "text-gray rounded-lg px-4",
        }))
    module_brand = forms.ChoiceField(label='Marca do módulo', choices=MODULE_BRAND_CHOICES, required=False, widget=forms.Select(
        attrs={
            'class': "text-gray rounded-lg px-4",
        }))
    roof = forms.ChoiceField(label='Tipos de telhado', choices=TYPES_ROOF_CHOICES, required=False, widget=forms.Select(
        attrs={
            'class': "text-gray rounded-lg px-4",
        }))
    order_by = forms.ChoiceField(label='Ordernar por', choices=ORDER_BY_CHOICES, required=False, widget=forms.Select(
        attrs={
            'class': "text-gray rounded-lg px-4",
        }))
    code = forms.CharField(label='Código', max_length=20, required=False, widget=forms.TextInput(
        attrs={
            'class': "text-gray rounded-lg px-4",
            'placeholder': 'Digite o código do kit',
            'autocomplete': 'off',
        }))
    amount_of_red_cables = forms.CharField(label='Quantidade de cabos vermelhos', required=False, widget=forms.NumberInput(
        attrs={
            'class': "text-gray rounded-lg px-4",
            'autocomplete': 'off'
        }))
    amount_of_black_cables = forms.CharField(label='Quantidade de cabos pretos', required=False, widget=forms.NumberInput(
        attrs={
            'class': "text-gray rounded-lg px-4",
            'autocomplete': 'off'
        }))
    quantity_stringbox = forms.CharField(label='Quantidade de stringbox', required=False, widget=forms.NumberInput(
        attrs={
            'class': "text-gray rounded-lg px-4",
            'autocomplete': 'off'
        }))
    