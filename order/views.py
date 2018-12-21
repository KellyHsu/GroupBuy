from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json
from deal.models import Order, Item

@csrf_exempt
def order_add(request):
    if request.method == 'POST':

        print(request.body)
        data = json.loads(request.body)
        # buyer_id = int(data['buyer_id'])
        for obj in data['json_all']:
            if int(obj['amount']) < 1:
                continue
            item = Item.objects.get(id=int(obj['item_id']))
            total = item.price * int(obj['amount'])
            order = Order.objects.create(buyer_id=int(data['user_id']), deal_id_id=int(obj['deal_id']), amount=int(obj['amount']), total=total, item_id_id=int(obj['item_id']), customer_field_1_val="yoyo")
            order.save()
        return JsonResponse({'success': 'True'})

    else:
        return JsonResponse({'success': 'YA'})


def my_order_view(request):

    return