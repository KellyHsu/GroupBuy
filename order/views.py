from .forms import OrderForm
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse


@csrf_exempt
def order_add(request):
    form = OrderForm(data=request.POST)
    print(form)
    print(form.cleaned_data['buyer_id'])

    if form.is_valid():
        # list_ = List.objects.create()
        # form.save(for_list=list_)
        return JsonResponse({'success': 'fall'})

    else:
        return JsonResponse({'success': 'YA'})


