from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import messages
from shopping_app.EmailBackEnd import EmailBackEnd
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect
from .models import Prodcut,Recharge,Profile,Booking,Kyc
from django.db.models import Q
import random,math

# Create your views here.
def home(request):
    return render(request,'homepage/home.html')


def product(request):
    product = Prodcut.objects.all()
    return render(request,'Products/product.html',{'product':product})

def product_detail(request,id):
    product = Prodcut.objects.get(id=id)
    # user = Profile.objects.get(user=request.user)
    # booking = Booking.objects.get(product=product)
    # if user.objects.filter(username = username).exists():
    #             messages.warning(request, "Username is already Taken")
    #             return redirect('signup')
    return render(request,'Products/product_detail.html',{'product':product})

def wallet(request):
    total_amount = 0
    user = Profile.objects.get(user=request.user)
    pr =Booking.objects.get(user=user)
    commission = pr.product.commission
   
    recharge = Recharge.objects.all()
    if recharge:
            for p in recharge:
                if p.recharge_request == "Accept":

                    total_amount += p.amount
                # print("total",total_amount)
    context = {
        'total_amount':total_amount,
        'commission':commission
    }
    return render(request,'Wallet/wallet.html',context)


def signup(request):
    
   
    return render(request,'signup/signup.html')

def otp(request):
    
    
    
    if request.method == "POST":
        # reference_no = request.POST.get("reference_no")
        username = request.POST.get("username")
        mobile = request.POST.get("mob_no")
        password = request.POST.get("password")
        otp_verfication = request.POST.get("otp_verfication")
        # print("verif",otp_verfication)
        otp = ""
        for i in range(1,7):
            a = random.random()
            b = math.floor(a*10)
            otp += str(b)
        
        print("hello",username,mobile,password,otp,otp_verfication)
        
        try:
            if User.objects.filter(username = username).exists():
                messages.warning(request, "Username is already Taken")
                return redirect('signup')
            
            if otp == otp_verfication:
                
                user = User.objects.create_user(username=username,password=password)
                user.profile.mobile = mobile  
            # user.save()
                messages.success(request,"Registration sucessfully Please Sign In ")
                return redirect("signin")      
            else:
                print("otp is not valid")
            
            
        except:
            messages.error(request,"somthing is wrong try again!!")
            return redirect("signup")
   
    return render(request,'Otp/otp.html')
def signin(request):

    if request.method == "POST":
        print("helloooo",request.POST.get("username"))
        print("helloooo",request.POST.get("password"))
        user=EmailBackEnd.authenticate(request,username=request.POST.get("username"),password=request.POST.get("password"))
        
        if user!=None:
            login(request,user)
            return redirect("home")
            # return HttpResponseRedirect('home')
           
           
        else:
            messages.error(request,"Invalid Login Or Password !!")
            return redirect('signin')
    
   

    return render(request,'signup/signin.html')



def profile(request):
    return render(request,'Profile/profile.html')    




# ---------------------------- Recharge ---------------------- 




def recharge(request):
    profile=Profile.objects.get(user=request.user)
    
    if request.method == "POST":
        upi_id = request.POST.get('upi_id')
        amount = int(request.POST.get('amount'))
        utr_no = request.POST.get('utr_no')
        if upi_id == "":
            messages.error(request,"select your Payment Modes")
            return redirect('recharge')
            
        if amount == "":
            messages.error(request,"Choose Your Amount")
            return redirect('recharge')

        

        
            
            
        try:
            
            recharge = Recharge.objects.create(user=profile,upi_id=upi_id,amount=amount,utr=utr_no)

            recharge.save()
            messages.success(request,"Recharge Successfull")
            return redirect('recharge')
            

        except:
            messages.error(request,"Something is Wrong Try Again !!")
            return redirect('recharge')
        

    return render(request,'Recharge/recharge.html')    

def recharge_history(request):
    recharge = Recharge.objects.all()
    return render(request,'transaction/recharge_history.html',{'recharge':recharge})

def withdraw_transaction(request):
    recharge = Recharge.objects.all()
    return render(request,'transaction/withdraw_transaction.html',{'recharge':recharge})



def booking(request):
    user = Profile.objects.get(user=request.user)
    product_id = request.GET.get('prod_id')
    print("sssss",product_id)
    product = Prodcut.objects.get(id=product_id)
    Booking(user=user,product=product).save()
    return redirect('home')


def myorder(request):
    user = Profile.objects.get(user=request.user)
    booking = Booking.objects.filter(user=user)
    context = {
        'booking':booking
    }
    return render(request,'orders/myorder.html',context)


def kyc(request):
    kyc = Kyc.objects.all()
    user = Profile.objects.get(user=request.user)
    if request.method == "POST":
        name = request.POST.get("name")
        bank_name = request.POST.get("bank_name")
        ac_no = request.POST.get("account_no")
        ifsc_code = request.POST.get("ifsc_code")
        try:
            kyc = Kyc.objects.create(user=user,bank_holder_name=name,bank_name=bank_name,account_number=ac_no,ifsc_code=ifsc_code)
            messages.success(request,f"{user} Kyc is updated")
            kyc.save()
        except:
            messages.error(request,"something is error Try Again !!")
            
    return render(request,'kyc/kyc.html',{'kyc':kyc})