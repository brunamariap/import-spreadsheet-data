import datetime
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
import openpyxl
from django.db import transaction
from .models import Kit

# Create your views here.


def homePage(request):

    # If this is a POST request then process the Form data
    if request.method == 'POST':
        file = request.FILES['archive']

        wb = openpyxl.load_workbook(file)

        # getting a particular sheet by name out of many sheets
        sheets = wb.sheetnames

        for sheet in sheets:
            worksheet = wb[sheet]

            for index, row in enumerate(worksheet.iter_rows()):
                if index == 0:
                    continue
                
                new_kit = Kit.objects.create(
                type_kit=sheet,
                identification=row[0].value,
                code=row[1].value,
                price=row[2].value,
                roof=row[3].value,
                connection=row[4].value,

                quantity_modules=row[5].value,
                module_model=row[6].value,
                module_unit_Wp_power=row[7].value,

                max_overload=row[8].value,
                kWp=row[9].value,

                inverter_1_quantity=row[10].value,
                inverter_1_model=row[11].value,
                inverter_2_quantity=row[12].value,
                inverter_2_model=row[13].value,

                amount_of_red_cables=row[14].value,
                model_red_cables=row[15].value,
                amount_of_black_cables=row[16].value,
                model_black_cables=row[17].value,

                quantity_pairs_connector=row[18].value,
                connector_pair_model=row[19].value,

                quantity_stringbox=row[20].value,
                model_stringbox=row[21].value,

                quantity_structure_1=row[22].value,
                model_structure_1=row[23].value,

                quantity_structure_2=row[24].value,
                model_structure_2=row[25].value,

                quantity_structure_3=row[26].value,
                model_structure_3=row[27].value,

                quantity_structure_4=row[28].value,
                model_structure_4=row[29].value,

                quantity_structure_5=row[30].value,
                model_structure_5=row[31].value,

                inverter_brand=row[32].value,
                module_brand=row[33].value,
            )

            new_kit.save()
        # for index, row in enumerate(excel_data):
        #     print(excel_data[index])
        """ 
            new_kit = Kit.objects.create(
                type_kit=sheet,
                identification=excel_data[index][0],
                code=excel_data[index][1],
                price=excel_data[index][2],
                roof=excel_data[index][3],
                connection=excel_data[index][4],

                quantity_modules=excel_data[index][5],
                module_model=excel_data[index][6],
                module_unit_Wp_power=excel_data[index][7],

                max_overload=excel_data[index][8],
                kWp=excel_data[index][9],

                inverter_1_quantity=excel_data[index][10],
                inverter_1_model=excel_data[index][11],
                inverter_2_quantity=excel_data[index][12],
                inverter_2_model=excel_data[index][13],

                amount_of_red_cables=excel_data[index][14],
                model_red_cables=excel_data[index][15],
                amount_of_black_cables=excel_data[index][16],
                model_black_cables=excel_data[index][17],

                quantity_pairs_connector=excel_data[index][18],
                connector_pair_model=excel_data[index][19],

                quantity_stringbox=excel_data[index][20],
                model_stringbox=excel_data[index][21],

                quantity_structure_1=excel_data[index][22],
                model_structure_1=excel_data[index][23],

                quantity_structure_2=excel_data[index][24],
                model_structure_2=excel_data[index][25],

                quantity_structure_3=excel_data[index][26],
                model_structure_3=excel_data[index][27],

                quantity_structure_4=excel_data[index][28],
                model_structure_4=excel_data[index][29],

                quantity_structure_5=excel_data[index][30],
                model_structure_5=excel_data[index][31],

                inverter_brand=excel_data[index][32],
                module_brand=excel_data[index][33],
            )

            new_kit.save() """

    context = {
        'form': '',
    }

    return render(request, 'home.html', context)
