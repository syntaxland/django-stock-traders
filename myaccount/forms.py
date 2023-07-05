from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import UserCreationForm
from .models import Profile
# from django.contrib.auth.password_validation import validate_password
from django.core.validators import MinLengthValidator


from captcha.fields import ReCaptchaField
from captcha.widgets import ReCaptchaV2Checkbox


# class ProfileRegistrationForm(forms.ModelForm):
class ProfileRegistrationForm(UserCreationForm):
    username = forms.CharField(
        max_length=40,
        validators=[MinLengthValidator(6)],
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}),
        required=True
    )
    first_name = forms.CharField(
        max_length=40,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name'}),
        required=True
    )
    last_name = forms.CharField(
        max_length=40,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name'}),
        required=True
    )
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
        required=True
    )
    phone_number = forms.CharField(
        max_length=20,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Phone Number'}),
        required=True
    )
    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}),
        max_length=100,
        required=True,
        # validators=[validate_password] 
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Confirm Password'}),
        required=True
    )
    # captcha = ReCaptchaField(widget=ReCaptchaV2Checkbox(attrs={'class': 'form-check-input'}))
    
    class Meta:
        model = Profile
        fields = ['username', 'first_name', 'last_name', 'email', 'phone_number', 'password1', 'password2'] 


# class ProfileLoginForm(forms.Form):
#     email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
#     required=True)
#     password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}),
#     required=True)
#     )

class ProfileLoginForm(forms.Form):
    identifier = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username or Email'}),
        required=True
    )

    # username = forms.CharField(
    #     widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}),
    #     required=True
    # )

    # email = forms.EmailField(
    #     widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
    #     required=True
    # )

    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}),
        required=True
    )

    # captcha = ReCaptchaField(widget=ReCaptchaV2Checkbox(attrs={'class': 'form-check-input'}))


class ForgetPasswordForm(forms.Form):
    email = forms.EmailField()
