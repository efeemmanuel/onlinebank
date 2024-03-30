from django.urls import path, include
from .views import *
app_name="appusers"



urlpatterns = [
    
    path('',index,name='index' ),
    path('about',about,name='about' ),
    path('card',card,name='card' ),
    path('loan',loan,name='loan' ),
    path('contact',contact,name='contact' ),
    path('signup', signup, name='signup'),
    path('login', user_login, name='login'),
    
    path('dashboard', dashboard, name='dashboard'),
    path('deposit', deposit, name='deposit'),
    path('local_transfer', local_transfer, name='local_transfer'),
    path('pin', pin, name='pin'),
    path('cards', cards, name='cards'),
    path('kyc', kyc, name='kyc'),
    path('loans', loans, name='loans'),
    path('success', success, name='success'),
    path('withdraw', withdraw, name='withdraw'),
    path('history', history, name='history'),

]