from django.db import models


# Create your models here.
class Bill(models.Model):
    amount = models.IntegerField(blank=True)
    type = models.CharField(max_length=50)





    def __str__(self):
        return self.id