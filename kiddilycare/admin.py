from django.contrib import admin
from .models import *

# Register your models here.
admin.site.site_header = "Kiddily Care | Admin panel"
admin.site.site_title = "Kiddily Care | Admin panel"
admin.site.index_title = "Kiddily Care | Admin panel"

admin.site.register(Customer)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(Provider)
admin.site.register(ShippingAddress)
admin.site.register(Article)


class ProductAdminImage(admin.StackedInline):
    model = ProductImage

class ProductAdminSpec(admin.StackedInline):
    model = Specification

class ProductAdminCharac(admin.StackedInline):
    model = Characteristic
 
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductAdminImage, ProductAdminSpec, ProductAdminCharac]
    fields = ('product_name', 'category', 'description', 'purchase_price', 'price', 'expiration_date', 'provider', 'isPromotional', 'promotion', 'product_main_image' )
 
    class Meta:
       model = Product
 
@admin.register(ProductImage)
class ProductAdminImage(admin.ModelAdmin):
    pass
 
@admin.register(Specification)
class ProductAdminSpec(admin.ModelAdmin):
    pass
 
@admin.register(Characteristic)
class ProductAdminCharac(admin.ModelAdmin):
    pass