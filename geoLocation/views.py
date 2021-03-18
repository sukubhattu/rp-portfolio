from django.shortcuts import render

import requests


def home(request):
    geodata = {}
    response = requests.get(
        "http://api.ipstack.com/103.58.145.247?access_key=d138f52b082f06731df94c1512290e9e"
    )
    geodata = response.json()
    return render(request, "home.html", {"geodata": geodata})
