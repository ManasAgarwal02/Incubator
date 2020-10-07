from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def home(request):
    return render(request, 'incubator/home.html')


def about(request):
    return render(request, 'incubator/about.html')


def analyze(request):
    my_url = request.POST.get("url")
    my_device = request.POST.get("device")
    print(f"URL: {my_url}  device : {my_device}")
    return render(request, 'incubator/analyze.html')
