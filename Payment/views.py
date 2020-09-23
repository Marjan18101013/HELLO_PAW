from django.shortcuts import render
from .models import Bill
# Create your views here.
def showBill(request):

    pay = Bill.objects.all()

    context ={

        'paybill': pay

    }

    return render(request,'Payment/ShowBill.html',context)