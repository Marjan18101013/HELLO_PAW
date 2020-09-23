from django.shortcuts import render
from .models import service
# Create your views here.
def showService(request):

    services = service.objects.all()

    context={
        'all_service': services
    }

    return render(request,'PetService/ShowService.html',context)