from django.shortcuts import render
from .models import Gainer
import requests
import json

# Create your views here.

url = 'https://www.nseindia.com/api/live-analysis-variations?index=gainers'
headers = {
    'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36',
    'Accept-Language':'en',
}
    
def index(request): 
    gainers = Gainer.objects.all()
    context = {
        "gainers" : gainers
    }
    return render(request, 'scrape/base.html', context)

