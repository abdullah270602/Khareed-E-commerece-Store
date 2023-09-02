from django.db import models

from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm

INPUT_CLASSES = 'w-full py-2 px-4 rounded-xl border-black-8 bg-gray-100'


class LogInForm(AuthenticationForm):
    username = forms.CharField(widget=forms.EmailInput(attrs = { 
                                                             'placeholder' : ' Email' ,
                                                             'class' : INPUT_CLASSES
                                                             }))
    
    password = forms.CharField(widget=forms.PasswordInput(attrs = { 
                                                             'placeholder' : ' Password' ,
                                                             'class' : INPUT_CLASSES
                                                             }))

class SignUpForm(UserCreationForm):   
    first_name  = forms.CharField(widget=forms.TextInput(attrs = { 
                                                                'placeholder' : ' First Name' ,
                                                                'class' : INPUT_CLASSES
                                                                })) 
    last_name  = forms.CharField(widget=forms.TextInput(attrs = { 
                                                                'placeholder' : ' Last Name' ,
                                                                'class' : INPUT_CLASSES
                                                                })) 

    username = forms.CharField(widget=forms.EmailInput(attrs = { 
                                                             'placeholder' : ' Email' ,
                                                             'class' : INPUT_CLASSES
                                                             }))
    
    password1 = forms.CharField(widget=forms.PasswordInput(attrs = { 
                                                             'placeholder' : ' Password' ,
                                                             'class' : INPUT_CLASSES
                                                             }))
    
    password2 = forms.CharField(widget=forms.PasswordInput(attrs = { 
                                                             'placeholder' : ' Confrim Passowrd' ,
                                                             'class' : INPUT_CLASSES
                                                             }))  

    class Meta:
        model = User
        fields = ['first_name','last_name','username','password1','password2']
        
        
        
