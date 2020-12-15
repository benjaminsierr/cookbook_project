from django.urls import path
from .views import signUpPageView, loginPageView, createUser, loginAttempt

urlpatterns = [
    path('signup/create', createUser, name='createUser'),
    path('signup', signUpPageView, name='signup'),
    path('login', loginAttempt, name='loginAttempt'),
    path('<failed>', loginPageView, name='login'),
    path('', loginPageView, name='login'),
]