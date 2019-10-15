import csv
from django.shortcuts import render


def inflation_view(request):
    template_name = 'inflation.html'
    context = {}
    with open('inflation_russia.csv') as file:
        header = file.readline().strip().split(';')
        data = csv.reader(file, delimiter=';')
        rows = [[row[0], *map(lambda x: float(x) if x else '-', row[1:-1]), row[-1]] for row in data]
        context['data_'] = rows
        context['header'] = header
    return render(request, template_name,
                  context)
