from django.shortcuts import render,redirect
from django.contrib.auth import login,authenticate,logout
from email_login.forms import RegistrationForm,AccountAuthentication
from django.http import HttpResponse
# # Create your views here.
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
            # email = form.cleaned_data.get('email').lower()
            # raw_password = form.cleaned_data.get('password1')
            # account = authenticate(email=email,password = raw_password )
            # login(request,account)
            # destination = get_rediect_if_exist(request)
            # if destination:  # if destination is not none 
            #     return redirect(destination)
            # return redirect('home')
            return redirect('login_user')
        else:
            form = RegistrationForm()
            context['registration_form'] =  form 


   
    return render(request,'email/register_user.html',context= {})









def loginUser(request,*args,**kwargs):

    context = {}
    user = request.user
    if user.is_authenticated:
        return redirect('home')
    destination = get_rediect_if_exist(request)
    if request.POST:
        form = AccountAuthentication(request.POST)
        if form.is_valid():
            email = request.POST['email']
            password = request.POST['password']
            user = authenticate(email=email,password = password )
            if user is not None:
                login(request,user)
                return redirect('home')
        else:
            context['login_form'] = form
    return render(request,'email/login_user.html',context={})


def get_rediect_if_exist(request):
    redirect = None
    if request.GET:
        if request.GET.get('next'):
            redirect = str(request.GET.get('next'))
    return redirect















def logoutUser(request):
    if request.method=='POST':
        logout(request)
        return redirect('home')
    else:
        return render(request,'email/logout_user.html') 