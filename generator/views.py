from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def home(request):
    return render(request, 'generator/home.html')


def password(request):
    this_pass = 'jaskd344_Sd'
    return render(request, 'generator/password.html', {'password': this_pass





                                                    })
