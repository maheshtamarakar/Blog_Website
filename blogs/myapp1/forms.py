#madded manually for forms 
from django import forms
from . models import blog

class Edit_Blog(forms.ModelForm):
    class Meta:#means ek class ek andar ek or class
         model = blog #jiske through ham ye form ready karna chahte h
         fields=('title', 'dsc')#those colums whose form i want to meke