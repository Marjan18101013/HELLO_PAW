from django.db import models
from Payment.models import Bill
# Create your models here.
class product(models.Model):
    p_name = models.CharField(max_length=100)
    p_cost = models.FloatField(blank=True)

    b_id =models.ForeignKey(Bill,on_delete=models.SET_NULL,null=True)


    def __str__(self):
        return self.p_name
