"""HELLO_PAW URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from Client import views as c_view
from PetShop import views as shop_view
from PetService import views as service_view
from  Payment import views as bill_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('OurClient',c_view.showCustomer),
    path('Shop',shop_view.showShop),
    path('Services',service_view.showService),
    path('payment',bill_view.showBill),
    path('Product_Sell/',c_view.CustomerProduct)


]
