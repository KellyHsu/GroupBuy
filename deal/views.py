from datetime import datetime

from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from .models import Deal, Item, Order


@login_required
def index(request):
    user_id = request.user.id
    print(user_id)
    deals = Deal.objects.filter(expired_time__gt=datetime.now())
    items = []
    # return "{0}/{1}".format(sum(ord.total for ord in obj.order_set.all()), obj.target_value)

    # for d in deals:
    for d in range(0, len(deals)):
        item = Item.objects.filter(deal_id=deals[d])
        items.append(item)
        # items[d] = item
    for obj in deals:
        s = sum(ord.total for ord in obj.order_set.all())
        # progress.append(s/obj.target_value)
        obj.prog = s/obj.target_value

    print(items)
    return render(request, 'deal/index.html', {"user_id": user_id, "deals": deals, "items": items})


@login_required
def my_order(request):
    user_id = request.user.id
    orders = Order.objects.filter(buyer_id=user_id)

    return render(request, 'deal/order.html', {"user_id":user_id,"orders": orders})
