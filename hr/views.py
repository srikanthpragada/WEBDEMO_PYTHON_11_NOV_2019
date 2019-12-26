from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
import requests


# Create your views here.

def index(request):
    return render(request, 'index.html')


def list_countries(request):
    resp = requests.get("https://restcountries.eu/rest/v2/all")
    if resp.status_code == 200:
        countries = sorted(resp.json(),
                           key = lambda c : c['population'],
                           reverse=True)
        return render(request, 'list_countries.html',
                      {'countries': countries})
    else:
        return HttpResponse("<h2>Sorry! Could not get details of countries!</h1>")


def country_info(request):
    if 'code' not in request.GET:
        return  HttpResponse("<h2>Sorry! Missing country code!</h2>")

    code = request.GET['code']   # code passed in URL
    resp = requests.get(f"https://restcountries.eu/rest/v2/alpha/{code}")
    if resp.status_code == 200:
        country = resp.json()
        return render(request, 'country_info.html',{'country': country})
    else:
        return HttpResponse("<h2>Sorry! Could not find country code!</h2>")

def ajax_demo(request):
    return render(request,'ajax_demo.html')

def ajax_datetime(request):
    return HttpResponse(str(datetime.now()))