from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'index.html')

def login(request):
    return render(request, 'login.html')

def register(request):
    return render(request, 'register.html')

def singleview(request):
    return render(request, 'singleview.html')

def propertyform(request):
    return render(request, 'sellform.html')

def buyform(request):
    return render(request, 'buyForm.html')