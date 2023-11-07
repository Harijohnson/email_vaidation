from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from .forms import UserModelForm,LoginUser
from django.contrib.auth.decorators import login_required, permission_required
from .models import * 
# Create your views here.
def home(request):
    context={}
    return render(request,'home.html',context)

def registerUser(request):
    if request.method == "POST":
        form = UserModelForm(request.POST)

        if form.is_valid():
            # email = request.POST['email']
            # password1 = request.POST['password1']
            # password2 = request.POST['password2']
            # user = UserManager._create_user(request,email=email,password1=password1,password2=password2)
            form.save()
            return redirect("login_user")
        else:
            print(form.errors)
    else:
        form = UserModelForm()
        context = {
        "form":form,
        }
        return render(request,'register_user.html',context)
    context = {
        "form":form,
    }
    return render(request,'register_user.html',context)

def loginUser(request):
    if request.method == "POST":
        form = LoginUser(request.POST)
        email = request.POST.get('email')
       
        password1 = request.POST.get('password1')
        print(email)
        print(password1)
        if form.is_valid():
            user =  authenticate(request,email = 'hari@gmail.com',
                                 password1 = 'Harikrishnan1@',
                                 )
            print('the user object is return ',user)
            if user is not None:
                login(request,user)
                return redirect('home')
            else:
                print('user is none')
        else:
            print('somthing is not good')
            print(form.errors)
            form = LoginUser()
            context = {
                "form":form,
            }
            return render(request,'login_user.html',context)
    else:

        form = LoginUser()
        context = {
        "form":form,
        }
        return render(request,'login_user.html',context)

def logoutUser(request):
    context={}
    return render(request,'logout_user.html',context)