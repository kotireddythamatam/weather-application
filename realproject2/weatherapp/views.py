from django.shortcuts import render
from django.http import HttpResponse
import requests
def input(request):
    return render(request,'input.html')
def data(request):
    a=request.POST['t1']
    b=request.POST['t2']
    c=request.POST['t3']
    d=a='http://api.openweathemap.org/data/2.5/weather?appid=0c42f7f6b53b244c78a418f4f181282a&q='
    e=requests.get(d, format(a)).json()
    return render(request,'data.html',{'f1':e})
