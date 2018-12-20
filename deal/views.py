from django.shortcuts import render
from .models import Deal

from django.contrib.auth.decorators import login_required


@login_required
def index(request):
    deals = Deal.objects.filter()
    # deals[0].item
    return render(request, 'deal/index.html', {"deals":deals})


