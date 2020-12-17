from django.urls import path
from .views import signUpPageView, loginPageView, loginAttempt, logout_view

urlpatterns = [
    path('signup', signUpPageView, name='signup'),
    path('login/logout', logout_view, name='logout'),
    path('login', loginAttempt, name='loginAttempt'),
    path('', loginPageView, name='login'),
]