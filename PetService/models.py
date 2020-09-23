from django.db import models
from Payment.models import Bill
# Create your models here.
class service(models.Model):
    s_Name = models.CharField(max_length=100)
    s_Cost = models.FloatField(blank=True)
    s_type = models.CharField(max_length=20)

    b_id = models.ForeignKey(Bill, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.s_Name