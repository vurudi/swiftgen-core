# admin.py
from django.contrib import admin
from .models import Order, Order_Requirements, DeliveryDetails

admin.site.register(Order)
admin.site.register(Order_Requirements)
admin.site.register(DeliveryDetails)
