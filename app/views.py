from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def about(request):
    return render(request,"about.html")
def booking(request):
    return render(request,"booking.html")
def contacts(request):
    return render(request,"contacts.html")
def department(request):
    return render(request,"department.html")
def doctors(request):
    return render(request,"doctors.html")
def  home(request):
    return render(request,"home.html")
    