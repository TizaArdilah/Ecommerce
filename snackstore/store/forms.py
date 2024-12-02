from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser
from .models import Product


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ["name", "description", "price", "stock", "image"]


from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = [
            "username",
            "email",
            "password1",
            "password2",
        ]  # Sesuaikan dengan field di model Anda
