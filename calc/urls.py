from django.urls import path
from . import views

urlpatterns = [
    path("",views.home,name="Home page"),
    path("index",views.index,name = "Index page"),
    path("result",views.add,name = "Result page")
]