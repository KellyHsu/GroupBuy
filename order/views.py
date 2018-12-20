from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json


@csrf_exempt
def order_add(request):
    if request.method == 'POST':
        received_json_data = json.loads(request.body)
        print(received_json_data)
        print(received_json_data['buyer_id'])
        return JsonResponse({'success': 'fall'})

    else:
        return JsonResponse({'success': 'YA'})


def my_order_view(request):

    return