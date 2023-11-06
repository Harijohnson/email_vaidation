from django.shortcuts import render

# Create your views here.
def home(request):
    context={}
    return render(request,'templates/home.html',context)

def registerUser(request):
    context={}
    return render(request,'templates/home.html',context)
def loginUser(request):
    context={}
    return render(request,'templates/home.html',context)
def logoutUser(request):
    context={}
    return render(request,'templates/home.html',context)