from django.shortcuts import render
from django.db.models import Q 
from .scraper import Scraper
# Create your views here.
def index(request):
     return render(request, "index.html", {})

def search(request):
    search_term = request.GET.get('search')
    
    scrapper=Scraper()
    scrapper.find(search_term)
    return render(request, "search.html", {

     })

def bucketlist(request):
     return render(request, "bucketlist.html", {})