from django.shortcuts import render,redirect

from .models import SellProperty

# Create your views here.
def index(request):

    details=SellProperty.objects.all()
    return render(request,'index.html',{'details':details})

def login(request):
    return render(request, 'login.html')

def register(request):
    return render(request, 'register.html')

def singleview(request, pk):
    details = SellProperty.objects.get(id=pk)
    return render(request, 'singleview.html',{'details':details})

def propertyform(request):

    if request.method == 'POST':
        newProperty = SellProperty()

        newProperty.name = request.POST['property']
        newProperty.owner = request.POST['owner']
        newProperty.price = request.POST['price']
        newProperty.phone = request.POST['phone']
        newProperty.landmark = request.POST['landmark']
        newProperty.description = request.POST['desc']
        newProperty.location = request.POST['location']
        newProperty.category = request.POST['cat']
        newProperty.image = request.FILES['image']
        newProperty.save()
        print('property Added Successfully')
        return redirect('/')
    else:
        return render(request, 'sellform.html')

def buyform(request):
    return render(request, 'buyForm.html')


def allProperties(request):
    properties = SellProperty.objects.all()
    return render(request,'allProperties.html',{'properties':properties})