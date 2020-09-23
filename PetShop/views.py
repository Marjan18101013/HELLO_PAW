from django.shortcuts import render
from .models import product
# Create your views here.
def showShop(request):

    products = product.objects.all()

    context = {
        'Products': products
    }


    return render(request, 'PetShop/ShowShop.html',context)