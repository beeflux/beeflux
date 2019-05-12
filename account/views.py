from django.http import HttpResponse
from django.shortcuts import render

def company_profile(request):
    return HttpResponse('<h1> This is the company app homepage </h1>')