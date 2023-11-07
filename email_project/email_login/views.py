from django.shortcuts import render,redirect
from django.contrib.auth import login,authenticate,logout
from email_login.forms import RegistrationForm
from django.http import HttpResponse
# Create your views here.
def home(request):
    context={}
    return render(request,'email/home.html',context)

def registerUser(request,*args,**kwargs):
    user = request.user
    if user.is_authenticated:
        return HttpResponse(f'You are alread authenticated as { user.email} .')
    context = {}
    if request.POST:
        form  = RegistrationForm(request.POST)
        if form.is_valid:
            form.save()
            email = form.cleaned_data.get('email').lower()
            raw_password = form.cleaned_data.get('password1')
            account = authenticate(email=email,password = raw_password )
            login(request,account)
            destination = kwargs.get('next')
            if destination:
                return redirect(destination)
            return redirect('home')
        else:
            form = RegistrationForm()
            context['registration_form'] =  form


   
    return render(request,'email/register_user.html',context)
























def loginUser(request):
    

    context = {
    }
    return render(request,'login_user.html',context)

def logoutUser(request):
    context={}
    return render(request,'logout_user.html',context)