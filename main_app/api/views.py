from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def main(request):
    return HttpResponse("HELLO")

def index(request):
    return render(request, 'frontend/index.html')