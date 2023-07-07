from django import forms
from django.contrib.auth.forms import AuthenticationForm, UsernameField
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.password_validation import validate_password
from django.core.validators import MinLengthValidator, RegexValidator

from phonenumber_field.formfields import PhoneNumberField
from phonenumber_field.widgets import PhoneNumberPrefixWidget

from captcha.fields import ReCaptchaField
from captcha.widgets import ReCaptchaV2Checkbox

from .models import Profile
from django.contrib.auth import get_user_model


User = get_user_model()


def clean_username(self):
        username = self.cleaned_data['username']
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError('Username is already taken. Please try another one.')
        return username


def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('Email already exists.')
        return email


def clean_phone_number(self):
        phone_number = self.cleaned_data['phone_number']
        if User.objects.filter(phone_number=phone_number).exists():
            raise forms.ValidationError('Phone number already exists.')
        return phone_number


class ProfileRegistrationForm(UserCreationForm):
    username = forms.CharField(
        max_length=40,
        validators=[MinLengthValidator(6)],
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}),
        required=True,
        error_messages={
            'required': 'Please enter your username.',
            'min_length': 'Username must be at least 6 characters long.',
        }
    )
    first_name = forms.CharField(
        max_length=40,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name'}),
        required=True,
        validators=[
            RegexValidator(
                r'^[a-zA-Z0-9]+$',
                'Only alphanumeric characters are allowed.'
            ),
        ],
        error_messages={
            'required': 'Please enter your first name.',
        }
    )
    last_name = forms.CharField(
        max_length=40,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name'}),
        required=True,
        validators=[
            RegexValidator(
                r'^[a-zA-Z0-9]+$',
                'Only alphanumeric characters are allowed.'
            ),
        ],
        error_messages={
            'required': 'Please enter your last name.',
        }
    )
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
        required=True,
        error_messages={
            'required': 'Please enter your email address.',
            'invalid': 'Please enter a valid email address.',
        }
    )
    phone_number = PhoneNumberField(
        widget=PhoneNumberPrefixWidget(attrs={'class': 'form-control', 'placeholder': 'Phone Number'}),
        max_length=14,
        required=True,
        error_messages={
            'required': 'Please enter your phone number.',
        }
    )
    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}),
        max_length=100,
        required=True,
        validators=[validate_password],
        error_messages={
            'required': 'Please enter your password.',
            'password_mismatch': 'Passwords do not match.',
        }
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Confirm Password'}),
        required=True,
        error_messages={
            'required': 'Please confirm your password.',
        }
    )
    # captcha = ReCaptchaField(widget=ReCaptchaV2Checkbox(attrs={'class': 'form-check-input'}))

    class Meta:
        model = Profile
        fields = ['username', 'first_name', 'last_name', 'email', 'phone_number', 'password1', 'password2']


class ProfileLoginForm(forms.Form):
    identifier = UsernameField(
        widget=forms.TextInput(attrs={'autofocus': True, 'class': 'form-control', 'placeholder': 'Username or Email'}),
        required=True,
        error_messages={
            'required': 'Please enter your username or email address.',
        }
    )
    password = forms.CharField(
        strip=False,
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}),
        required=True,
        error_messages={
            'required': 'Please enter your password.',
        }
    )
      
    # captcha = ReCaptchaField(widget=ReCaptchaV2Checkbox(attrs={'class': 'form-check-input'}))


class ForgetPasswordForm(forms.Form):
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
        required=True,
        error_messages={
            'required': 'Please enter your email address.',
            'invalid': 'Please enter a valid email address.',
        }
    )


# from django import forms
# from django.contrib.auth.forms import AuthenticationForm
# from django.contrib.auth.forms import UserCreationForm
# from .models import Profile
# # from django.contrib.auth.password_validation import validate_password
# from django.core.validators import MinLengthValidator

# from phonenumber_field.formfields import PhoneNumberField
# from phonenumber_field.widgets import PhoneNumberPrefixWidget

# from captcha.fields import ReCaptchaField
# from captcha.widgets import ReCaptchaV2Checkbox


# # class ProfileRegistrationForm(forms.ModelForm):
# class ProfileRegistrationForm(UserCreationForm):
#     username = forms.CharField(
#         max_length=40,
#         validators=[MinLengthValidator(6)],
#         widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}),
#         required=True
#     )
#     first_name = forms.CharField(
#         max_length=40,
#         widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name'}),
#         required=True
#     )
#     last_name = forms.CharField(
#         max_length=40,
#         widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name'}),
#         required=True
#     )
#     email = forms.EmailField(
#         widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
#         required=True
#     )
#     phone_number = PhoneNumberField(
#         widget=PhoneNumberPrefixWidget(attrs={'class': 'form-control', 'placeholder': 'Phone Number',}),
#         max_length=14,
#         required=True, 
#     )
#     password1 = forms.CharField(
#         widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}),
#         max_length=100,
#         required=True,
#         # validators=[validate_password] 
#     )
#     password2 = forms.CharField(
#         widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Confirm Password'}),
#         required=True
#     )
#     captcha = ReCaptchaField(widget=ReCaptchaV2Checkbox(attrs={'class': 'form-check-input'}))
    
#     class Meta:
#         model = Profile
#         fields = ['username', 'first_name', 'last_name', 'email', 'phone_number', 'password1', 'password2'] 


# # class ProfileLoginForm(AuthenticationForm):
# class ProfileLoginForm(forms.Form):
#     identifier = forms.CharField(
#         widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username or Email'}),
#         required=True
#     )

#     # username = forms.CharField(
#     #     widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}),
#     #     required=True
#     # )

#     # email = forms.EmailField(
#     #     widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
#     #     required=True
#     # )

#     password = forms.CharField(
#         widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}),
#         required=True
#     )

#     captcha = ReCaptchaField(widget=ReCaptchaV2Checkbox(attrs={'class': 'form-check-input'}))


# class ForgetPasswordForm(forms.Form):
#     email = forms.EmailField()
