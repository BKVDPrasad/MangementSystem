from django import forms
from .models import LoginModel,NewuserModel,ThoughtModel

class LogiForm(forms.ModelForm):
    type = (
        ('admin', 'ADMIN'),
        ('user', 'USER'),
    )
    type = forms.ChoiceField(choices=type)
    password=forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = LoginModel
        fields = '__all__'



class NewuserForm(forms.ModelForm):
    username = forms.CharField(max_length=30,label='User Name')
    emailid = forms.EmailField(label='Email ID')
    companynaem = forms.CharField(max_length=30,label='Company Name')
    password = forms.CharField(widget=forms.PasswordInput)
    dateofbirth = forms.DateField(input_formats="%d %B, %Y",label='DOB')


    class Meta:
        model = NewuserModel
        fields = '__all__'

class ThoughtForm(forms.ModelForm):
    class Meta:
        model = ThoughtModel
        fields ="__all__"
