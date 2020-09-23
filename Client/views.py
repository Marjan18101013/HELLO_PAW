from django.shortcuts import render
from .models import Customer
# Create your views here.
def showCustomer(request):

    customer = Customer.objects.all()

    context = {
        'all_customer': customer
    }

    return render(request,'Client/ShowClients.html',context)

def CustomerProduct(request):



    return render(request,'Client/Cproduct.html')
