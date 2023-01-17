from django.shortcuts import render

# Create your views here.
def dashboard(request):
    return render(request,'admin/index.html')

def properties(request):
    return render(request,'admin/allproperties.html')

def singleprop(request):
    return render(request,'admin/single.html')