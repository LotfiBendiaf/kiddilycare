from django.contrib import admin
from .models import *

# Register your models here.
admin.site.site_header = "Kiddily Care | Admin panel"
admin.site.site_title = "Kiddily Care | Admin panel"
admin.site.index_title = "Kiddily Care | Admin panel"

admin.site.register(Customer)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(Product)
admin.site.register(Provider)
admin.site.register(ShippingAddress)
admin.site.register(Article)
