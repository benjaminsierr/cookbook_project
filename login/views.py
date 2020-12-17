from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import redirect
from .forms import SignupForm, LoginForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
# Create your views here.

#sign up view
#just routes to the sign up page
def signUpPageView(request):
    form = SignupForm(request.POST or None)
    if form.is_valid():
        form.save()

        username = form.cleaned_data['username']
        password = form.cleaned_data['password1']
        user = authenticate(username=username, password=password)
        login(request,user)
        return redirect('index')
    context = {
        'form' : form,
    }
    return render(request, 'login/signup.html', context)

#log in view
#just routes to the log in page
def loginPageView(request):
    form = LoginForm(request = request, data = request.POST)
    if form.is_valid():
        username = form.cleaned_data.get('username')
        print('========================',username)
        password = form.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request,user)
            return redirect('index')
    context = {
        'form' : form,
    }
    return render(request, 'login/login.html',context)

def loginAttempt(request):
    return redirect('login')
    
def logout_view(request):
    logout(request)
    return redirect('index')
    
#def profilePageView(request)
#Do this if we have time