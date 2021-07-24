from django.http.response import HttpResponse
from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request, 'index.html')


def result(request):
    maintainer = "siva"
    try:
        return HttpResponse("Hi <h1>{0} {1} </h1> by<h4>{2}</h4>".format(request.POST.get("first_name"), request.POST.get("last_name"),maintainer))
    except Exception as e:
        return HttpResponse("{}".format(e))