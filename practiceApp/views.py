from django.shortcuts import render

def mobile_views(request):
    mobiles = [
        {"name": "iPhone 14", "price": 799, "brand": "Apple"},
        {"name": "Samsung Galaxy S23", "price": 999, "brand": "Samsung"},
        {"name": "Google Pixel 7", "price": 599, "brand": "Google"},
    ]
    return render(request, "mobiles.html", {"mobiles": mobiles})
    
def laptop_view(request):
    Laptops = [
        {"name":"macbook","price":100000,"brand":"apple"},
        {"name":"legion","price":60000,"brand":"lenovo"},
        {"name":"Nitro","price":70000,"brand":"acer"}
    ]
    return render(request,"laptop.html",{"Laptops":Laptops})