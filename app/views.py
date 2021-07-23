from django.http.response import HttpResponse
from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request, 'index.html')


def result(request):
    return HttpResponse("Hi <h1>{0} {1}</h1>".format(request.POST.get("first_name"), request.POST.get("last_name")))
