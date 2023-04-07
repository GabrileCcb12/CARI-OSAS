from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1','password2'] #PERMITE QUE EL FORMULARIO PIDA ESTOS DATOS MAS Y NO SOLO EL NOMBRE DE USUARIO Y LA CONTRASEÑA
class LoginForm(forms.Form):
    username = forms.CharField(label='Usuario', max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label='Contraseña', max_length=100, widget=forms.PasswordInput(attrs={'class': 'form-control'}))
