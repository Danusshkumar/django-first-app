from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request,'add.html')

def add(request):
    val1 = int(request.GET['num1'])
    val2 = int(request.GET['num2'])
    sum = val1 + val2
    return render(request, 'result.html',{"result" : sum})

def index(request):
    return render(request,'index.html')