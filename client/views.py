from django.shortcuts import render, redirect
from . models import Client
from django.contrib import messages
# Create your views here.



def cuppon(request):
    context={
        "button": 0
        
    }
    c= Client.objects.all()
    cuppon_sum = []
    if request.method == "POST":
        phone = request.POST.get("phone")      
          
        if phone in str(c):
            if phone:
                c = Client.objects.filter(phone__contains=phone)
                for i in c:
                    cuppon_num=i.cuppon
                    context.update({
                        "num":cuppon_num
                    })
                    
                    for i in range(1, cuppon_num+1):
                        cuppon_sum.append(i)
                    context.update({
                        "sum":cuppon_sum,
                        "button": 1
                    })
            else:
                messages.add_message(request, messages.ERROR, '등록되지 않거나 잘못된 번호입니다')
                    
        else:
            messages.add_message(request, messages.ERROR, '등록되지 않거나 잘못된 번호입니다')
            
    return render(request,'client/cuppon.html', context)


def signup(request):
    num=0
    c = Client.objects.all()
    if request.method == "POST":
        name = request.POST.get("name")
        phone = request.POST.get("phone")
        
        if not phone in str(c):
            for i in phone:
                num+=1
            if num == 11:
                Client(name = name, phone=phone, cuppon=0).save()
                return redirect('index')
            else:
                messages.add_message(request, messages.ERROR, '이미등록됬거나 잘못된 번호입니다')
                
        else:
            messages.add_message(request, messages.ERROR, '이미등록됬거나 잘못된 번호입니다')
           
            
        
    return render(request, 'client/signup.html')