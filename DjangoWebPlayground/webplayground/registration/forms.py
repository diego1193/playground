from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile

class UserCreationFormWithEmail(UserCreationForm):
    # Email ya existe en el modelo User solo estamos especificando que los queremos utilizar
    email = forms.EmailField(required=True, help_text="Requerido, 254 caracteres como máximo y debe ser valido") 

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def clean_email(self):
        email = self.cleaned_data.get("email")
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("El email ya está registrado, prueba con otro.")
        return email


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ["avatar", "bio", "link"]
        widgets = {
            "avatar": forms.ClearableFileInput(attrs={"class": "form-control-file my-3"}),
            "bio": forms.Textarea(attrs={'class': 'form-control'}),
            "link": forms.URLInput(attrs={"class": "form-control mt-3", "placeholder": "Link"}),
        }

class EmailForm(forms.ModelForm):
    email = forms.EmailField(required=True, help_text="Requerido, 254 caracteres como máximo y debe ser valido") 

    class Meta:
        model = User
        fields = ['email']

    def clean_email(self):
        email = self.cleaned_data.get("email")
        if 'email' in self.changed_data:
            if User.objects.filter(email=email).exists():
                raise forms.ValidationError("El email ya está registrado, prueba con otro.")
        return email