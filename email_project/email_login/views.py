from django.shortcuts import render

# Create your views here.
def home(request):
    context={}
    return render(request,'home.html',context)

def registerUser(request):
    context={}
    return render(request,'register_user.html',context)
def loginUser(request):
    context={}
    return render(request,'login_user.html',context)
def logoutUser(request):
    context={}
    return render(request,'logout_user.html',context)