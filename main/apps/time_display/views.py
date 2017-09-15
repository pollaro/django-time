from django.shortcuts import render, redirect, HttpResponse
from time import gmtime, strftime

def index(request):
    currtime = {'time':strftime('%B %-d, %Y %-I:%M %p',gmtime())}
    return render(request,'time_display/index.html',currtime)
