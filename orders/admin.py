from django.contrib import admin
from orders.models import Order

# admin.site.register(Order)

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display=['size',
                  'order_status',
                  'quantity',
                  'created',
                  'updated',
                  ]
    list_filter=['created','order_status',]