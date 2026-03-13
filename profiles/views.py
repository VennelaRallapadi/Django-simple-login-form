from django.shortcuts import render
from django.http import HttpResponse
# Create your views here. 

def Profiles(request):
    #return HttpResponse("<h1>profiles</h1>")
    return render(request,'profiles.html',{})