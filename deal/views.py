from django.shortcuts import render
from django.http import HttpResponse
from deal.models import Deal

# Create your views here.
def index(request):
    deals = Deal.objects.filter()
    return render(request, 'deal/index.html', {"deals":deals})