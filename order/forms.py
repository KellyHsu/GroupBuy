from django import forms


class OrderForm(forms.Form):

    buyer_id = forms.IntegerField()
    item_id = forms.IntegerField()
    amount = forms.IntegerField()
    deal_id = forms.IntegerField()