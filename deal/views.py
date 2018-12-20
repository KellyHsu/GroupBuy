from django.shortcuts import render
from django.http import HttpResponse
from .models import Deal, Item

# Create your views here.
def index(request):
    deals = Deal.objects.filter()
    items={}
    # for d in deals:
    for d in range(0, len(deals)):
        item = Item.objects.filter(deal_id=deals[d])
        # items.append(item)
        items[d] = item
    print(items)
        # print(item[0].name)
    return render(request, 'deal/index.html', {"deals":deals,"items":items})
