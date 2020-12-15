from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.models import User
# Create your views here.

#sign up view
#just routes to the sign up page
def signUpPageView(request):
    return render(request, 'login/signup.html')

#log in view
#just routes to the log in page
def loginPageView(request, failed = False):
    
    context = {
        'logintext' : failed
    }
    return render(request, 'login/login.html', context)

def loginAttempt(request, failed = False):
    print('---------email-----------', request.POST.get('email'))
    user = User.objects.get(email = request.POST.get('email'))
    if user.password == request.POST.get('password'):
        return redirect('index')
    else:
        failed = True
        return redirect('login', failed)
    

def createUser(request):
    email = request.POST.get('email')
    firstname = request.POST.get('firstname')
    lastname = request.POST.get('lastname')
    password = request.POST.get('password')
    username = str(request.POST.get('email')) + str(request.POST.get('firstname'))
    user = User.objects.create_user(email=email, password = 'password', username = username, first_name = firstname, last_name = lastname)
    
    print('----------------',user)
    user.save()
    return redirect('login')
    
#def profilePageView(request)
#Do this if we have time