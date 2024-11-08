from django.shortcuts import render,get_object_or_404
from .models import My_Cars

# Create your views here.

def mainproject(request):
    rohn = My_Cars.objects.all()
    return render(request,'mainproject.html',{"rohn":rohn})

def nextproject(request, rohan_id):
    rohan = get_object_or_404(My_Cars,pk=rohan_id)
    return render(request,'nextproject.html',{"rohan":rohan})

