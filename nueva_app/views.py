from django.shortcuts import render

# Create your views here.

def m1(request):
    msj = {"mensaje":"Te amo Luca <3"}
    return render(request,"nueva_app/index.html",msj)