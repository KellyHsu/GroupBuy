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
    remarks = models.CharField(max_length=255)
    buyers = models.ManyToManyField(User, verbose_name="list of buyers")


# class Item(models.Model):
#     name = models.CharField(max_length=30)
#     price = models.FloatField()
#     amount = models.IntegerField()
#     buyer = models.ForeignKey()
#     customer_field_1_val = models.CharField(max_length=10)
#     customer_field_2_val = models.CharField(max_length=10)


class DealAdmin(admin.ModelAdmin):
    readonly_fields = ["card_pic_image"]
    list_display = ['name', "store", "author", "card_pic_image"]


    def card_pic_image(self, obj):
        return mark_safe('<img src="{url}" width="{width}" height={height} />'.format(
            url=obj.card_pic.url,
            width=obj.card_pic.width,
            height=obj.card_pic.height,
        )
        )


#
# class Menu():
#     deal_id
#     name
#     cost_per_item
#     amount
#     custom_field1Desc
#     custom_field1Val
#     custom_field2Desc
#     custom_field2Val
#
#
# class UserDeal(models.Model):
#     user_id
#     deal_id
admin.site.register(Deal, DealAdmin)
