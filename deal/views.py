from django.shortcuts import render
from django.http import HttpResponse
from .models import Deal

# Create your views here.
def index(request):
    deals = Deal.objects.filter()
    # deals[0].item
    return render(request, 'deal/index.html', {"deals":deals})