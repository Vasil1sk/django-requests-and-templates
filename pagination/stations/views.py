from django.shortcuts import render, redirect
from django.urls import reverse
from django.core.paginator import Paginator
from django.conf import settings
import csv


def index(request):
    return redirect(reverse('bus_stations'))

def bus_stations(request):
    with open(settings.BUS_STATION_CSV, 'r', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        stations_list = list(reader)
    page_number = request.GET.get('page', 1)
    paginator = Paginator(stations_list, 10)
    page = paginator.get_page(page_number)
    context = {
        'bus_stations': page,
        'page': page,
    }
    return render(request, 'stations/index.html', context)