from django.shortcuts import render
from django.http import HttpResponse
import json
import requests
import pandas as pd
import urllib
from urllib import request
import requests
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

    if my_url[len(my_url) - 1] == "/":
        my_url = my_url[0:len(my_url) - 1]
    print(f"URL: {my_url}  device : {my_device}")
    url = f"https://www.googleapis.com/pagespeedonline/v5/runPagespeed?url={my_url}/&strategy={my_device}"

    # API request
    result = urllib.request.urlopen(url.format(url)).read().decode('UTF-8')
    result_json = json.loads(result)

    print(result_json["lighthouseResult"]["audits"]["cumulative-layout-shift"]["displayValue"])
    context = {
        "my_device": my_device,
        "my_url": my_url,
        "overall_category": result_json["loadingExperience"]["overall_category"],
        "cumulative_layout_shift": result_json["lighthouseResult"]["audits"]["cumulative-layout-shift"],
        "largest_contentful_paint": result_json["lighthouseResult"]["audits"]["largest-contentful-paint"],
        "first_input_delay": result_json["loadingExperience"]["metrics"]["FIRST_INPUT_DELAY_MS"],
        "first_contentful_paint": result_json["lighthouseResult"]["audits"]["first-contentful-paint"],
        "interactive": result_json["lighthouseResult"]["audits"]["interactive"],
        "total_blocking_time": result_json["lighthouseResult"]["audits"]["total-blocking-time"],
        "speed_index": result_json["lighthouseResult"]["audits"]["speed-index"]
    }

    return render(request, 'incubator/analyze.html', context)


def network_request(request):
    my_url = request.POST.get("url")
    my_device = request.POST.get("device")
    print(f"URL: {my_url}  device : {my_device}")
    APIKey = "AIzaSyALIsdCRDWuduGIy071_x5lOFsVgyq3WaE"

    if my_url[len(my_url) - 1] == "/":
        my_url = my_url[0:len(my_url) - 1]
    print(f"URL: {my_url}  device : {my_device}")
    url = f"https://www.googleapis.com/pagespeedonline/v5/runPagespeed?url={my_url}/&strategy={my_device}"

    # API request
    result = urllib.request.urlopen(url.format(url)).read().decode('UTF-8')
    result_json = json.loads(result)

    print(result_json["lighthouseResult"]["audits"]["network-requests"]["description"])
    network = {
        "title": result_json["lighthouseResult"]["audits"]["network-requests"]["description"],
        "net": result_json["lighthouseResult"]["audits"]["network-requests"]["details"]["items"]
    }
    return render(request, 'incubator/network_request.html', network)


