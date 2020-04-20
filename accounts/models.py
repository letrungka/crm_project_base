from django.db import models

# Create your models here.
class Customer(models.Model):
  name = models.CharField(max_length=200)
  phone = models.CharField(max_length=13, null=True)
  email = models.CharField(max_length=200, null=True)
  date_created = models.DateTimeField(auto_now_add=True)

  def __str__(self):
    return self.name

class Tag(models.Model):
  name = models.CharField(max_length=200, null=True)

  def __str__(self):
    return self.name

class Product(models.Model):

  CATELOGY = (
    ('Indoor', 'Indoor'),
    ('Outdoor', 'Outdoor'),
  )
  name = models.CharField(max_length=200)
  price = models.FloatField(null=True)
  catalogy = models.CharField(max_length=200, null=True, choices=CATELOGY)
  description = models.CharField(max_length=200, null=True, blank=True)
  date_created = models.DateTimeField(auto_now_add=True)
  tags = models.ManyToManyField(Tag)

  def __str__ (self):
    return self.name

class Order(models.Model):
  STATUS = (
    ('Pending','Pending' ),
    ('Out of delivery', 'Out of delivery'),
    ('Delivered', 'Delivered'),
  )
  customer = models.ForeignKey(Customer,null=True, on_delete=models.SET_NULL)
  #product = models.ForeignKey(Product,null=True, on_delete=models.SET_NULL)
  product = models.ManyToManyField(Product)
  cost = models.FloatField(null=True)
  date_created = date_created = models.DateTimeField(auto_now_add=True)
  status = models.CharField(max_length=20, null=True, choices=STATUS)
  

# product1 = Product.objects.get(id=1)
# tags = Tag.objects.filter(product=product1)

# orders = Order.objects.all()
# order1 = orders.first()
# products =  Product.objects.filter(order=order1)

# usId1 = Customer.objects.get(id=1)
# orders = Order.objects.filter(customer=usId1)

# usId1 = Customer.objects.get(id=1)
# chairOder = cusId1.order_set.filter(product__name="chair")

#