from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


# Create your models here.
class Customer(models.Model):


    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    customer_name = models.CharField(max_length=100, null=True, blank=False)
    customer_email = models.EmailField(null=True, blank=False)
    customer_phone = models.CharField(max_length=20, null=True, blank=True, default="+")
    customer_address = models.CharField(max_length=200, null=True, blank=True)
    

    def __str__(self):
        return self.customer_name


class Provider(models.Model):

    provider_name = models.CharField(max_length=100, null=True, blank=False)
    provider_email = models.EmailField(null=True, blank=False)
    provider_address =models.CharField(max_length=200, null=True, blank=True)
    provider_phone = models.CharField(max_length=20, null=True, blank=False, default="+")
    provider_activty = models.CharField(max_length=100, null=True, blank=False)

    def __str__(self):
        return "%s %s" % (self.provider_name, str(self.id))

class Product(models.Model):

    class Promotion(models.TextChoices):
        PROMO = 'Promo'
        NO_PROMO = 'No Promo'
    
    CATEGORY = (
        ('Beauté', 'Beaute'),
        ('Santé', 'Sante'),
        ('Accessoires', 'Accessoires'),
        ('Visage', 'Visage'),
        ('Corps', 'Corps'),
        ('Ete', 'Ete'),
        ('PierresJade', 'PierresJade'),
    )

    product_name = models.CharField(max_length=200, null=True, blank=False)
    purchase_price = models.FloatField(null=True, blank=False)
    price = models.DecimalField(max_digits=7, decimal_places=2, default=0)
    provider = models.ForeignKey(Provider, on_delete=models.SET_NULL, default="provider introuvable", null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    expiration_date = models.DateField(null=True, blank=True)
    product_image = models.ImageField(null=True, default="Icon.png")
    quantity = models.IntegerField(null=True, blank=True, default=30)
    description = models.TextField(null=True, blank=True)
    category = models.CharField(max_length=100, null=True, choices=CATEGORY)
    digital = models.BooleanField(default=False)
    tax = models.FloatField(null=True, blank=True, default=0)
    isPromotional = models.CharField(max_length=20, choices=Promotion.choices, default=Promotion.NO_PROMO)
    promotion = models.FloatField(null=True, blank=True, default=0)
    qr_code = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.product_name

    @property
    def imageURL(self):
        try:
            url = self.product_image.url
        except:
            url = ''
        return url

    @property
    def margin(self):
        return self.price-self.purchase_price

class Order(models.Model):

    class Status(models.TextChoices):
        PENDING = 'Pending'
        IN_PROGRESS = 'In Progress'
        CONFIRMED = 'Confirmed'
        CANCELED = 'Canceled'
        DELIVERED = 'Delivered'

    transaction_id = models.CharField(max_length=200, null=True)
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True, blank=True)
    order_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=Status.choices, default=Status.PENDING)
    comment = models.TextField(null=True, blank=True, default='Please put here any comment')

    def __str__(self):
        return str(self.id)
    
    @property
    def shipping(self):
        shipping = False
        orderItems = self.orderitem_set.all()
        for orderItem in orderItems:
            if orderItem.product.digital == False:
                shipping = True
        return shipping
    
    @property
    def get_cart_total(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.get_item_total for item in orderitems])
        return total

    @property
    def get_cart_items(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.quantity for item in orderitems])
        return total

class OrderItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True, default="Product")
    order = models.ForeignKey(Order, on_delete=models.CASCADE, null=True)
    quantity = models.IntegerField(default=0, null=True, blank=True)
    
    def __str__(self):
        return str(self.product) + ' x' + str(self.quantity) 

    @property
    def get_item_total(self):
        item_total = self.product.price * self.quantity
        return item_total
    
class ShippingAddress(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
    address = models.CharField(max_length=200, null=False)
    country = models.CharField(max_length=200, null=False, default="Country")
    city = models.CharField(max_length=200, null=False)
    state = models.CharField(max_length=200, null=False)
    zipcode = models.CharField(max_length=200, null=False)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.address

class Article(models.Model):

    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    text = models.TextField()
    date = models.DateField()

    def get_absolute_url(self):
        return reverse('article', args=[str(self.id)])

    def __str__(self): 
        return self.title