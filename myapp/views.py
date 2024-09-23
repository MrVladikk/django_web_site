from django.shortcuts import render
from django.http import HttpResponse
import datetime

# Create your views here.

def current_datetime(request):
    now = datetime.datetime.now()
    html = f"<html><body>Current date and time: {now}.</body></html>"
    return HttpResponse(html)

def multiplication_table(request):
    table = "<table border='1'>"
    for i in range(1, 11):
        table += "<tr>"
        for j in range(1, 11):
            table += f"<td>{i * j}</td>"
        table += "</tr>"
    table += "</table>"
    return HttpResponse(f"<html><body>{table}</body></html>")


def programmer_day(request):
    current_year = datetime.datetime.now().year
    programmer_day = datetime.datetime(current_year, 1, 1) + datetime.timedelta(days=255)
    html = f"<html><body>Programmer's Day in {current_year}: {programmer_day.date()}.</body></html>"
    return HttpResponse(html)

def home(request):
    return HttpResponse("<h1>Главная страница города</h1>")

def news(request):
    return HttpResponse("<h1>Новости города</h1>")

def management(request):
    return HttpResponse("<h1>Руководство города</h1>")

def facts(request):
    return HttpResponse("<h1>Факты о городе</h1>")

def contacts(request):
    return HttpResponse("<h1>Контактные телефоны городских служб</h1>")

def history(request):
    return HttpResponse("<h1>Общая информация об истории города</h1>")

def history_people(request):
    return HttpResponse("<h1>Известные жители города</h1>")

def history_photos(request):
    return HttpResponse("<h1>Исторические фотографии города</h1>")

def home(request):
    return HttpResponse('''
        <h1>Главная страница города</h1>
        <ul>
            <li><a href="/news/">Новости города</a></li>
            <li><a href="/management/">Руководство города</a></li>
            <li><a href="/facts/">Факты о городе</a></li>
            <li><a href="/contacts/">Контакты</a></li>
            <li><a href="/history/">История города</a></li>
        </ul>
    ''')