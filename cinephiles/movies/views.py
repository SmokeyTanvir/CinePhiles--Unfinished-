from django.shortcuts import render
from flask import request

# Create your views here.
def home(request):
    return render(request, 'home.html')