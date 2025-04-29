import time
from django.shortcuts import render

from practiceApp.models import Mobile,Laptop

def mobile_views(request):
    # mobiles = [
    #     {"name": "iPhone 14", "price": 799, "brand": "Apple"},
    #     {"name": "Samsung Galaxy S23", "price": 999, "brand": "Samsung"},
    #     {"name": "Google Pixel 7", "price": 599, "brand": "Google"},
    # ]
    mobiles = Mobile.objects.all()
    return render(request, "mobiles.html", {"mobiles": mobiles})
    
def laptop_view(request):
    # Laptops = [
    #     {"name":"macbook","price":100000,"brand":"apple"},
    #     {"name":"legion","price":60000,"brand":"lenovo"},
    #     {"name":"Nitro","price":70000,"brand":"acer"}
    # ]
    Laptops= Laptop.objects.all()
    return render(request,"laptop.html",{"Laptops":Laptops})

def add_new_mobile(request):
    if request.method == "GET":

        return render(request,"add_new_mobiles.html")
    if request.method == "POST":
        brand = request.POST.get('brand')
        model = request.POST.get('model')
        price = request.POST.get('price')
        # print(f"the brand is {brand} and the model is {model} and the price is {price}")
        Mobile.objects.create(brand = brand , name = model , price = price)
        return render(request,"success_page.html")

def update_mobile(request):
    if request.method == "GET":
        mobile_id = request.GET.get('id')
        mobile_var = Mobile.objects.get(id=mobile_id)
        return render(request,"update_mobile.html",{"mobile" : mobile_var})
    
    if request.method == "POST":
        mobile_id = request.POST.get('mobile_id')
        brand = request.POST.get('brand')
        model = request.POST.get('model')
        price = request.POST.get('price')
        print(f"brand : {brand} and model {model} and price {price} and mobile id = {mobile_id}")
        update_mobile = Mobile.objects.get(id = mobile_id)
        # print(f"brand : {brand} and model {model} and price {price}")
        update_mobile.brand = brand
        update_mobile.name = model
        update_mobile.price = price
        update_mobile.save()
        return render(request,"success_page.html")

def success_page(request):
    return render(request,"success_page.html")

def add_new_Laptop(request):
    if request.method == 'GET':
        return render(request,"add_new_laptop.html")
    if request.method == "POST":
        brand = request.POST.get("brand")
        model = request.POST.get('model')
        price = request.POST.get('price')
        Laptop.objects.create(brand = brand,name = model,price = price)
        return render(request,"success_page.html")

    
def update_laptop(request):
    if request.method == 'GET':
        laptop_id=request.GET.get('id')
        laptop_Var=Laptop.objects.get(id=laptop_id)
        return render(request,"update_laptop.html",{'laptop':laptop_Var})
    
    if request.method == "POST" :
        laptop_id = request.POST.get('laptop_id')
        laptop_brand = request.POST.get('brand')
        laptop_model = request.POST.get('model')
        laptop_price = request.POST.get('price')
        laptop_Update = Laptop.objects.get(id = laptop_id)

        laptop_Update.brand = laptop_brand
        laptop_Update.name = laptop_model
        laptop_Update.price = laptop_price
        laptop_Update.save() 
        return render(request,"success_page.html")