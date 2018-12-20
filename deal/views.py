from django.shortcuts import render
from django.http import HttpResponse
from .models import Deal, Item

from django.contrib.auth.decorators import login_required


@login_required
def index(request):
    user_id = request.user.id
    print(user_id)
    deals = Deal.objects.filter()
    items=[]
    # for d in deals:
    for d in range(0, len(deals)):
        item = Item.objects.filter(deal_id=deals[d])
        items.append(item)
        # items[d] = item
    print(items)
        # print(item[0].name)
    return render(request, 'deal/index.html', {"user_id":user_id,"deals":deals,"items":items})
