from django.db import models
from PetShop.models import product
from PetService.models import service
# Create your models here.
class Customer(models.Model):
    name = models.CharField(max_length=100)
    Address = models.CharField(max_length=200)
    Phone = models.IntegerField(blank=True)
    pet_type = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class CustomerProduct(models.Model):
    c_id = models.ForeignKey(Customer, on_delete=models.SET_NULL,null=True, blank=True)
    p_id = models.ForeignKey(product, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.Customer.name + " : " + self.product.p_name

class CustomerService(models.Model):
    c_id = models.ForeignKey(Customer,on_delete=models.SET_NULL,null=True)
    s_id = models.ForeignKey(service,on_delete=models.SET_NULL,null=True)

    def __str__(self):
        return self.Customer.name + " : " + self.service.s_Name





