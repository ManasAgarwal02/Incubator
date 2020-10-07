from django.shortcuts import render
from django.http import HttpResponse
import json
import requests
import pandas as pd
import urllib
from urllib import request

import time
import io


# Create your views here.

def home(request):
    return render(request, 'incubator/home.html')


def about(request):
    return render(request, 'incubator/about.html')


def analyze(request):
    my_url = request.POST.get("url")
    my_device = request.POST.get("device")
    APIKey = "AIzaSyALIsdCRDWuduGIy071_x5lOFsVgyq3WaE"
    # print(f"URL: {my_url}  device : {my_device}")
    url = f"https://www.googleapis.com/pagespeedonline/v5/runPagespeed?url={my_url}/&strategy={my_device}"

    # API request
    result = urllib.request.urlopen(url).read().decode('UTF-8')
    # print(result)
    result_json = json.loads(result)
    # with open('result.json', 'w') as f:
    #     json.dump(result_json, f)

    return render(request, 'incubator/analyze.html')
