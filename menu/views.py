from django.shortcuts import render, redirect
from .models import MainMenu,BasicMenu,CoffeeMenu,DrinkMenu,InariMenu,SetMenu,SideMenu

# Create your views here.


def sushi(request):
    m = MainMenu.objects.all()
    kind = "스시"
    context={
        "mset": m,
        "kind":kind,
    }
    return render(request, 'menu/sushi.html', context)

def basic(request):
    m = BasicMenu.objects.all()
    kind = "단품"
    context={
        "kind":kind,
        "mset":m
    }
    return render(request, 'menu/sushi.html', context)

def coffee(request):
    m = CoffeeMenu.objects.all()
    kind = "커피/에이드"
    context={
        "kind":kind,
        "mset":m
    }
    return render(request, 'menu/sushi.html', context)

def drink(request):
    m = DrinkMenu.objects.all()
    kind = "음료/주류"
    context={
        "kind":kind,
        "mset":m
    }
    return render(request, 'menu/sushi.html', context)

def inari(request):
    m = InariMenu.objects.all()
    kind = "토핑유부"
    context={
        "mset":m,
        "kind":kind,
    }
    return render(request, 'menu/sushi.html', context)

def set(request):
    m = SetMenu.objects.all()
    kind = "세트"
    context={
        "mset":m,
        "kind":kind,
    }
    return render(request, 'menu/sushi.html', context)

def side(request):
    m = SideMenu.objects.all()
    kind = "사이드"
    context={
        "mset":m,
        "kind":kind,
    }
    return render(request, 'menu/sushi.html', context)