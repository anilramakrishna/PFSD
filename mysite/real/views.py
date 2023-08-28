from email import message
from multiprocessing import context
from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth import login,logout,authenticate
from django.contrib import messages

from .models import *
from .forms import *
from django.contrib.auth.decorators import login_required
from .decoraters import *
from django.contrib.auth.models import Group
from django.conf import settings  
from django.core.mail import send_mail 
from django.contrib.auth.models import User
def registerUser(request):
    form = CreateUserForm()
    custform=CustomerForm()
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            custform=CustomerForm(request.POST)
            if form.is_valid() and custform.is_valid():
                user=form.save()
                customer=custform.save(commit=False)
                customer.user=user
                customer.email=form.cleaned_data['email']
                customer.save()
                messages.success(request,'account created successfully')
                return redirect('login')
        context={'form':form}
        return render(request,'home1/register.html',context)
@unautheticated_user
def loginpage(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user = authenticate(username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            messages.info(request,"Username or Password is incorrect")

    return render(request,'home1/login.html')
@admin_only
def home(request):
    group=request.user.groups.all()[0].name
    context={'group':group}
    return render(request,'home1/home.html',context)
@login_required(login_url='login')
def logoutUser(request):
    logout(request)
    return redirect('home')
@login_required(login_url='login')    
def property(request):
    property2=submit_order.objects.filter(delete_status=False)
    context={'property2':property2}
    return render(request,'home1/properties.html',context)
@login_required(login_url='login')
def submit(request):
    initial_dict = {
        'name':request.user.username
    }
    form=CustomerSubmitPropertyForm(initial=initial_dict)
    if request.method == 'POST':
        request.POST._mutable = True
        request.POST['name'] = request.user.get_username()
        form = CustomerSubmitPropertyForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request,'Your Property is Submitted Sucessfully')
        else:
            messages.MessageFailure(request,'enter the valid details')
    context={'form':form}
    return render(request,'home1/submit_properties.html',context)
@login_required(login_url='login')
def contact(request):
    con=ContactForm()
    if request.method == 'POST':
        con=ContactForm(request.POST)
        if con.is_valid():
            con.save()
            messages.success(request,'Your form is Submitted Sucessfully')
    context={'con':con}
    return render(request,'home1/contact_us.html',context)

@login_required(login_url='login')  
def account(request):
    # user=request.user
    # print(user)
    user_details = Rcustomer.objects.filter(user=request.user)
    user_details = list(user_details)
    
    user = user_details[0]
    form = CustomerForm1(instance=user)
    context={'form':form}
    if request.method=="POST":
        form = CustomerForm1(request.POST, request.FILES,instance=user)
        if form.is_valid():
            form.save()
    return render(request,'home1/account.html',context)

def management(request):
    Customer=Rcustomer.objects.all()
    coninf=contact_us.objects.all()
    Property=submit_order.objects.filter(delete_status=False)
    Deleted_Properties=submit_order.objects.filter(delete_status=True)
    context={'Customer':Customer,'Property':Property, 'Deleted_Properties': Deleted_Properties,'coninf':coninf}
    return render(request,'home1/management.html',context)

def update(request, pk):
    order=submit_order.objects.get(id=pk)
    form=Update(instance=order)
    if request.method=='POST':
        form=Update(request.POST, instance=order)
        if form.is_valid():
            form.save()
            return redirect('management')
    context={'form':form}
    return render(request,'home1/update_form.html',context)

def delete_order(request, pk):
    order=submit_order.objects.get(id=pk)
    if request.method=='POST':
        submit_order.objects.filter(id=pk).update(delete_status=True)
        return redirect('management')
    context={'item':order}
    return render(request,'home1/delete.html',context)

@login_required(login_url='login') 
def orders(request):
    print(request.user.username)
    user_properties = submit_order.objects.filter(name=request.user.username)
    context = {'properties':user_properties} 
    return render(request,'home1/order.html',context)
    

def reopen_order(request, pk):
    submit_order.objects.filter(id=pk).update(delete_status=False)
    return redirect('management')

def customer(request, pk):
    customer=Rcustomer.objects.get(id=pk)
    Customer1=Rcustomer.objects.all()
    property = submit_order.objects.filter(name=request.user.username)
    context={'customer':customer,'property':property,'Customer1':Customer1}
    return render(request,'home1/customer.html',context)

@login_required(login_url='login') 
def duplex(request):
    dup=submit_order.objects.filter(delete_status=False)
    context={'dup':dup}
    return render(request,'home1/duplex.html',context)
@login_required(login_url='login') 
def villa(request):
    vill=submit_order.objects.filter(delete_status=False)
    context={'vill':vill}
    return render(request,'home1/villa.html',context)
@login_required(login_url='login') 
def beach(request):
    beach=submit_order.objects.filter(delete_status=False)
    context={'beach':beach}
    return render(request,'home1/Beach_House.html',context)
@login_required(login_url='login') 
def appartment(request):
    app=submit_order.objects.filter(delete_status=False)
    context={'app':app}
    return render(request,'home1/appartment.html',context)
@login_required(login_url='login') 
def commercial(request):
    com=submit_order.objects.filter(delete_status=False)
    context={'com':com}
    return render(request,'home1/commercial.html',context)
@login_required(login_url='login') 
def rental(request):
    ren=submit_order.objects.filter(delete_status=False)
    context={'ren':ren}
    return render(request,'home1/rental.html',context)

def sign(request):
    form=UserCreationForm()
    if request.method == 'POST':
        form=UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
    context={'form':form}
    return render(request,'home1/sign.html',context)



    


