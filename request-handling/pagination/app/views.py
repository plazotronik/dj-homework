import csv
from urllib import parse
from django.core.paginator import Paginator
from django.shortcuts import render_to_response, redirect
from django.urls import reverse

from app.settings import BUS_STATION_CSV

with open(BUS_STATION_CSV, encoding='cp1251') as file:
    raw = csv.DictReader(file)
    list_bus = []
    for row in raw:
        list_bus.append(dict(row))

def index(request):
    return redirect(reverse(bus_stations))


def bus_stations(request):
    page_num = request.GET.get('page')
    paginator = Paginator(list_bus, 10)
    page_bst = paginator.get_page(page_num)
    current_page = page_bst.number
    if page_bst.has_previous():
        pr_page_num = {'page': current_page - 1}
        prev_page_url = reverse(bus_stations) + '?' + parse.urlencode(pr_page_num)
    else:
        prev_page_url = None
    if page_bst.has_next():
        nx_page_num = {'page': current_page + 1}
        next_page_url = reverse(bus_stations) + '?' + parse.urlencode(nx_page_num)
    else:
        next_page_url = None
    return render_to_response('index.html', context={
        'bus_stations': page_bst.object_list,
        'current_page': current_page,
        'prev_page_url': prev_page_url,
        'next_page_url': next_page_url,
    })

