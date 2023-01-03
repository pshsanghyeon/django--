from django.shortcuts import render, redirect
from .models import Cart
from menu.models import CoffeeMenu, MainMenu, SetMenu, SideMenu, DrinkMenu, BasicMenu, InariMenu
from client.models import Client
from django.contrib import messages
# Create your views here.

def cupponuse(request):
    cset = Cart.objects.all()
    client = Client.objects.all()
    if request.method == "POST":
        phone = request.POST.get("phone")
        if phone:
            if phone in str(client):
                c = Client.objects.filter(phone__contains=phone)

                
                for i in c:
                    if i.cuppon == 10:
                        i.cuppon = 0
                        i.save()
                        for j in Cart.objects.all():
                            if str(j.kind) == "coffee":
                                if j.price > 0:
                                    j.price = 0
                                    j.save()
                                    break
                            # return redirect("cart:cart")
                    else:
                        messages.add_message(request, messages.ERROR, '물고기가 부족해요!')
                        
         

        else:
            messages.add_message(request, messages.ERROR, '등록되지 않거나 잘못된 번호입니다')
            return redirect("cart:cart")
            
    return redirect("cart:cart")

def buy(request):
    cset = Cart.objects.all()
    client = Client.objects.all()
    
    if request.method == "POST":
        phone = request.POST.get("phone")
        if phone in str(client):
            for i in cset:
                if i.price >= 9900:
                    c = Client.objects.filter(phone__contains=phone)
                    for j in c:
                        j.cuppon += 1
                        j.save()
                        cset.delete()
                        return render(request,'done.html')
            else:
                pass
        else:
            messages.add_message(request, messages.ERROR, '등록되지 않거나 잘못된 번호입니다')
    
    return redirect("cart:cart")

def addcart(request, pk, mpk):
    menu_set = [CoffeeMenu, MainMenu, SetMenu, SideMenu, DrinkMenu, BasicMenu, InariMenu]
    for i in menu_set:
        m = i.objects.filter(name__contains = pk)
        for j in m:
            Cart(name = j.name, price = j.price, num = 1, img = j.img, kind = j.kind).save()
    return redirect(f'menu:{mpk}')


def remove(request, pk):
    c = Cart.objects.get(id=pk)
    c.delete()
    
    
    return redirect('cart:cart')



def cart(request):
    cset = Cart.objects.all()
    cart_sum = 0
    for i in cset:
        cart_sum += i.price

    context={
        "cset":cset,
        "cart_sum": cart_sum
    }
    return render(request,'cart.html', context)