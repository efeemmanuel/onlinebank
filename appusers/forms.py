from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
#from .models import CustomerInfo
from .models import *
from django.contrib.auth.forms import PasswordChangeForm



class RegisterForm(UserCreationForm):
    username = forms.CharField(max_length=30, required=True, widget=forms.TextInput(attrs={'class': 'form-control','style': 'max-width: 750px;', 'placeholder': 'Enter username'}))
    email = forms.CharField(max_length=30, required=True, widget=forms.EmailInput(attrs={'class': 'form-control','style': 'max-width: 750px;', 'placeholder': 'Enter email address'}))
    password1 = forms.CharField(max_length=30, required=True, widget=forms.PasswordInput(attrs={'class': 'form-control','style': 'max-width: 750px;', 'placeholder': 'Set password'}))
    password2 = forms.CharField(max_length=30, required=True, widget=forms.PasswordInput(attrs={'class': 'form-control','style': 'max-width: 750px;', 'placeholder': 'Confirm password'}))

    class Meta:
        model=User
        fields = ['username','email','password1','password2'] 
        
        

class LoginForm(forms.Form):
    username = forms.CharField(max_length=30, required=True, widget=forms.TextInput(attrs={'class': 'form-control','style': 'max-width: 750px;', 'placeholder': 'Enter username'}))
    password = forms.CharField(max_length=30, required=True, widget=forms.PasswordInput(attrs={'class': 'form-control','style': 'max-width: 750px;', 'placeholder': 'Set password'}))
    
    

class KYCForm(forms.ModelForm):
    class Meta:
        model = KYC
        fields = '__all__'
    
class LoanRequestForm(forms.ModelForm):
    class Meta:
        model = LoanRequest
        fields = ['amm', 'credit', 'ten', 'pur']
    
    
    
    
 
    
    
class DepositForm(forms.ModelForm):
    class Meta:
        model = Deposit
        fields = ['amount', 'deposit_slip']
        

class LocalTransferForm(forms.ModelForm):
    class Meta:
        model = LocalWithdrawal
        fields = ['account_number', 'iban','swiftcode', 'amount']
        


class WithdrawForm(forms.ModelForm):
    class Meta:
        model = Withdraw
        exclude = ['user']
        


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'phone', 'subject', 'message']


class PinVerificationForm(forms.Form):
    pin = forms.CharField(max_length=6, widget=forms.PasswordInput(attrs={'class': 'form-control form-control-xl', 'placeholder': 'Enter PIN', 'required': True}))
    
    
    
    
    