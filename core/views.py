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

        excel_data = list()
        for sheet in sheets:
            worksheet = wb[sheet]

            for row in worksheet.iter_rows():
                row_data = list()
                for cell in row:
                    row_data.append(cell.value)
                    
                excel_data.append(row_data)


        """ 
        for index, row in enumerate(excel_data):
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
