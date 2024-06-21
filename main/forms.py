from django import forms 
from .models import Profile, Contact 
from django import forms 
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm 
from django.contrib.auth.models import User 
from django.core.exceptions import ValidationError 


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)
    phone_number = forms.CharField(max_length=15, required=True)
    first_name = forms.CharField(max_length=30, required=True)
    last_name = forms.CharField(max_length=30, required=True)

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'phone_number', 'password1', 'password2']

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise ValidationError('Этот email уже используется.')
        return email


    def save(self, commit=True):
        user = super(UserRegisterForm, self).save(commit=False)
        user.username = self.cleaned_data['email']
        user.email = self.cleaned_data['email']
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.phone_number = self.cleaned_data['phone_number']
        if commit:
            user.save()
        return user
 
 
class UserLoginForm(AuthenticationForm): 
    username = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'class': 'form-control'})) 
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-control'})) 
 
class ProfileForm(forms.ModelForm):
    first_name = forms.CharField(max_length=30, required=True)
    last_name = forms.CharField(max_length=30, required=True)
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']



class ContactForm(forms.ModelForm): 
    email = forms.EmailField(required=True) 
 
    class Meta: 
        model = Contact 
        fields = ['first_name', 'last_name', 'age', 'sport', 'phone', 'email'] 
        widgets = {
            'first_name': forms.Textarea(attrs={'rows': 1, 'cols': 40, 'style': 'resize:none;'}),
            'last_name': forms.Textarea(attrs={'rows': 1, 'cols': 40, 'style': 'resize:none;'}),
            'age': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Возраст'}),
            'sport': forms.Textarea(attrs={'rows': 1, 'cols': 40, 'style': 'resize:none;'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Телефон', 'pattern': '[0-9]{11}', 'title': 'Введите 10 цифр телефона', 'style': 'resize:none; width:100%; height:2em;'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email', 'style': 'resize:none; width:100%; height:2em;'}),
        }