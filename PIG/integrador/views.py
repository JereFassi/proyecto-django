# Create your views here.
from datetime import datetime
from django.shortcuts import render
from django.http import HttpResponse

def index(request):

    context = {
        "hoy": datetime.now
    }

    return render(request,'integrador/index.html', context)