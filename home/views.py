from django.shortcuts import render, redirect
from django.contrib import messages
from .models import SellProperty, Customer, Buyer,EmiRequest
from django.contrib.auth.models import User, auth, Group
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from django.http import HttpResponseRedirect
from django.urls import reverse

from .decorators import unauthenticated_user, allowed_users, admin_only

# Create your views here.

# ----Home Page --------


def index(request):
    details = SellProperty.objects.filter(status__icontains='Approved')
    customer = Customer.objects.all()
    group = None
    if request.user.groups.exists():
        group = request.user.groups.all()[0].name

    if group == 'admin':
        return HttpResponseRedirect(reverse('dashboard'))
    if group == 'bank':
        return HttpResponseRedirect(reverse('bank'))
    if group == 'customer':
        return render(request, 'index.html', {'details': details,'customer':customer})

    return render(request, 'index.html', {'details': details})

# -------Register Page-------


@unauthenticated_user
def register(request):
    if request.method == 'POST':
        # ['fname'] is name attribute from form
        first_name = request.POST['fname']
        last_name = request.POST['lname']
        user_name = request.POST['uname']
        email = request.POST['email']
        pwd = request.POST['pwd']
        cpwd = request.POST['cpwd']

        #  check pass is equal and email and username are unique
        if pwd == cpwd:
            if User.objects.filter(username=user_name).exists():
                print('username taken')
                messages.info(request, 'username taken')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                print('email taken')
                messages.info(request, 'email taken')
                return redirect('register')
        # to register these date in database
            else:
                user = User.objects.create_user(
                    username=user_name, email=email, first_name=first_name, last_name=last_name, password=pwd)
                user.save()
                group = Group.objects.get(name='customer')
                user.groups.add(group)
                Customer.objects.create(
                    user=user,
                    name=user.username
                )
                print('user created successfully ')
                messages.info(request, 'user created successfully')
                return redirect('login')
        else:
            print('password not matching ')
            messages.info(request, 'password not matching')
            return redirect('register')

    else:
        return render(request, 'register.html')

# ------Login Page---------


@unauthenticated_user
def loginUser(request):

    if request.method == 'POST':
        username = request.POST['email']
        password = request.POST['pwd']

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            print('username or password is incorrect')
            return redirect('login')
    else:
        return render(request, 'login.html')

# ----Logout User------


def logoutUser(request):
    logout(request)
    return redirect('index')


# -----Single Property Page------
@login_required(login_url='login')
def singleview(request, pk):
    details = SellProperty.objects.get(id=pk)
    return render(request, 'singleview.html', {'details': details})


# -----SellProperty Form------
@login_required(login_url='login')
def propertyform(request,pk):
    customer = Customer.objects.get(id=pk)
    customer1 = Customer.objects.filter(id=pk)
    if request.method == 'POST':
        newProperty = SellProperty(customer=customer)

        newProperty.name = request.POST['property']
        newProperty.owner = request.POST['owner']
        newProperty.price = request.POST['price']
        newProperty.phone = request.POST['phone']
        newProperty.landmark = request.POST['landmark']
        newProperty.description = request.POST['desc']
        newProperty.bed = request.POST['bed']
        newProperty.baths=request.POST['baths']
        newProperty.location = request.POST['location']
        newProperty.category = request.POST['cat']
        newProperty.image = request.FILES['image']
        newProperty.save()
        print('property Added Successfully')
        return redirect('/')
    else:
        context={'customer':customer1, 'customer1':customer}
        return render(request, 'sellform.html',context)


# --------BuyProperty Form-------------
@login_required(login_url='login')
def buyform(request,pk):
    property = SellProperty.objects.get(id=pk)
    cust = Customer.objects.get(name=request.user.username)
    if request.method == 'POST':
        buyer = Buyer(property=property, customer=cust)
        buyer.dob = request.POST['dob']
        buyer.payment = request.POST['pay']
        buyer.name = request.POST['bname']
        buyer.save()
        return redirect('/')
    else:
        context={'property':property}
        return render(request, 'buyForm.html',context)


# --------------------Emi Request Form ---------------------
@login_required(login_url='login')
def emi_request(request,pk):
    property = SellProperty.objects.get(id=pk)
    cust = Customer.objects.get(name=request.user.username)
    if request.method == 'POST':
        emi = EmiRequest(property=property, customer=cust)
        emi.name = request.POST['bname']
        emi.dob = request.POST['dob']
        emi.bankName = request.POST['bank']
        emi.bankBranch = request.POST['branch']
        emi.emiYear = request.POST['years']
        emi.emiAmount = request.POST['amount']

        emi.save()
        return redirect('/')
    else:
        context={'property':property}
        return render(request,'emiForm.html',context)




# ---------All Properties Page--------
@login_required(login_url='login')
def allProperties(request):
    if 'search' in request.GET:
        search = request.GET['search']
<<<<<<< HEAD
        properties = SellProperty.objects.filter(location__icontains=search)
    else:
        properties = SellProperty.objects.filter(status__icontains='Approved')
    return render(request, 'allProperties.html', {'properties': properties})


# --------User Dashboard---------
@allowed_users(allowed_roles=['customer'])
def userDashboard(request, pk_test):
    customer = Customer.objects.filter(id=pk_test)
    customer1 = Customer.objects.get(id=pk_test)
    props = customer1.sellproperty_set.all()
    propsCount = customer1.sellproperty_set.all().count


    buys = customer1.buyer_set.all()
    buyCount = customer1.buyer_set.all().count

    # Buy details

    context={
        'customer':customer,
        'customer1':customer1,
        'props':props, 
        'propsCount':propsCount,
        'buys':buys,
        'buyCount':buyCount
        }
    return render(request, 'userDash.html',context)

# ----------------------------------------------------------------------------------



























# -----------------------Admin Dashboard-----------------------------------
@allowed_users(allowed_roles=['admin'])
@login_required(login_url='login')
def dashboard(request):
    details = SellProperty.objects.filter(status__icontains='Approved')
    propCount = details.count
    total = SellProperty.objects.all().count
    userCount = Customer.objects.all().count

    context = {'details': details,
               'propCount': propCount, 
               'userCount': userCount,
               'total':total
               }

    return render(request, 'adm/index.html', context)


@allowed_users(allowed_roles=['admin'])
def properties(request):
    all = SellProperty.objects.all()
    return render(request, 'adm/allproperties.html',{'all':all})


@allowed_users(allowed_roles=['admin'])
def singleprop(request):
    return render(request, 'adm/single.html')


def logoutAdm(request):
    logout(request)
    return redirect('index')


def edit(request, id):
    Data = SellProperty.objects.get(id=id)
    return render(request, 'adm/editForm.html', {'Data': Data})


def formUpdate(request, id):
    if request.method == 'POST':
        newProperty = SellProperty.objects.get(id=id)

        newProperty.name = request.POST['property']
        newProperty.owner = request.POST['owner']
        newProperty.price = request.POST['price']
        newProperty.phone = request.POST['phone']
        newProperty.landmark = request.POST['landmark']
        newProperty.description = request.POST['description']
        newProperty.type = request.POST['type']
        newProperty.status = request.POST['status']
        newProperty.save()
        print('property Added Successfully')
        return redirect('dashboard')
    else:
        return render(request, 'adm/editForm.html')

# ----------------------------------------------------------------------------------
# --------------------Bank Dashboard---------------------


@allowed_users(allowed_roles=['bank'])
def bank(request):

    allDetails = EmiRequest.objects.all()
    reqCount = EmiRequest.objects.all().count
    return render(request, 'buyerDetails.html',{'allDetails':allDetails,'reqCount':reqCount})
=======
        properties = SellProperty.objects.filter(location__icontains = search)
    else:
        properties = SellProperty.objects.all()
    return render(request,'allProperties.html',{'properties':properties})

>>>>>>> 8e6d2074cd529905884115526fafecb64bc17d5d
