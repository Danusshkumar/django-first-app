from django.shortcuts import render

# Create your views here.
def portfolio(request):
    return render("templates/index.html",name="Home")