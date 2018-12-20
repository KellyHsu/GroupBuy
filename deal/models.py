from django.contrib import admin
from django.db import models
from django.utils.safestring import mark_safe
from django.utils.timezone import now
from django.contrib.auth.models import User


class Deal(models.Model):
    name = models.CharField(max_length=30)
    store = models.CharField(max_length=30)
    card_pic = models.ImageField()
    author = models.CharField(max_length=30)
    desc = models.CharField(max_length=255)
    expired_time = models.DateTimeField(default=now, blank=True)
    remarks = models.CharField(max_length=255, blank=True, null=True)
    buyers = models.ManyToManyField(User, verbose_name="list of buyers", null=True, blank=True)
    target_value = models.FloatField()


class Item(models.Model):
    name = models.CharField(max_length=30)
    price = models.FloatField()
    amount = models.IntegerField(default=0)
    # buyer = models.ForeignKey(User, on_delete=models.CASCADE)
    customer_field_1_desc = models.CharField(max_length=10, blank=True, null=True)
    # customer_field_1_val = models.CharField(max_length=10, blank=True, null=True)
    customer_field_2_dec = models.CharField(max_length=10, blank=True, null=True)
    # customer_field_2_val = models.CharField(max_length=10, blank=True, null=True)
    deal_id = models.ForeignKey(Deal, on_delete=models.CASCADE)
    # is_paid = models.BooleanField(default=False)


class Order(models.Model):
    buyer = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.IntegerField(default=0)
    total = models.FloatField(default=0.)
    deal_id = models.ForeignKey(Deal, on_delete=models.CASCADE)
    item_id = models.ForeignKey(Item, on_delete=models.CASCADE)
    is_paid = models.BooleanField(default=False)
    customer_field_1_val = models.CharField(max_length=10, blank=True, null=True)
    customer_field_2_val = models.CharField(max_length=10, blank=True, null=True)


class ItemAdmin(admin.ModelAdmin):
    pass


class MenuItemsInline(admin.TabularInline):
    model = Item


class OrderInline(admin.TabularInline):
    model = Order


class DealAdmin(admin.ModelAdmin):
    readonly_fields = ["card_pic_image"]
    list_display = ['name', "store", "author", "card_pic_image", "progress"]
    inlines = [
        MenuItemsInline,
        OrderInline
    ]

    def card_pic_image(self, obj):
        return mark_safe('<img src="{url}" width="{width}" height={height} />'.format(
            url=obj.card_pic.url,
            width=128,
            height=128,
        )
        )

    def progress(self, obj):
        return "{0}/{1}".format(sum(ord.total for ord in obj.order_set.all() ),obj.target_value)


admin.site.register(Deal, DealAdmin)
admin.site.register(Item, ItemAdmin)

# Reporter.objects.filter(article__pk=1)
