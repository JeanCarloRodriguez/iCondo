from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request, userName):
    return render(request, "iCondo/index.html", {
        "userName": userName
    })