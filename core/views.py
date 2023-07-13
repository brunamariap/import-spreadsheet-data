import datetime
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
import openpyxl
# Create your views here.
def homePage(request):

    # If this is a POST request then process the Form data
    if request.method == 'POST':
        file = request.FILES['archive']

        wb = openpyxl.load_workbook(file)

        # getting a particular sheet by name out of many sheets
        sheets = wb.sheetnames

        for sheet in sheets:
            excel_data = list()
            worksheet = wb[sheet]
            
            for row in worksheet.iter_rows():
                row_data = list()
                for cell in row:
                    row_data.append(str(cell.value))
                excel_data.append(row_data)

            print(excel_data)

    context = {
        'form': '',
    }

    return render(request, 'home.html', context)