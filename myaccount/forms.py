from django import forms
from django.contrib.auth.forms import AuthenticationForm, UsernameField
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import PasswordChangeForm, SetPasswordForm

from django.contrib.auth.password_validation import validate_password
from django.core.validators import MinLengthValidator, RegexValidator

from phonenumber_field.formfields import PhoneNumberField
from phonenumber_field.widgets import PhoneNumberPrefixWidget

from captcha.fields import ReCaptchaField
from captcha.widgets import ReCaptchaV2Checkbox

from .models import Profile
from django.contrib.auth import get_user_model

from django.contrib.auth.forms import UserChangeForm
# from .models import UserProfile

User = get_user_model()


class ProfileRegistrationForm(UserCreationForm):
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


class PasswordResetRequestForm(forms.Form):
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
        required=True,
        error_messages={
            'required': 'Please enter your email address.',
            'invalid': 'Please enter a valid email address.',
        }
    )


class CustomPasswordChangeForm(PasswordChangeForm):
    error_messages = {
        'password_mismatch': 'The two password fields didn’t match.',
        'password_incorrect': 'Your old password was entered incorrectly. Please enter it again.',
    }

    old_password = forms.CharField(
        label='Old Password',
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Old Password'}),
        strip=False,
    )
    new_password1 = forms.CharField(
        label='New Password',
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'New Password'}),
        strip=False,
    )
    new_password2 = forms.CharField(
        label='Confirm New Password',
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Confirm New Password'}),
        strip=False,
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['old_password'].label = 'Old Password'
        self.fields['old_password'].widget.attrs['class'] = 'form-control'
        self.fields['old_password'].widget.attrs['placeholder'] = 'Old Password'

        self.fields['new_password1'].label = 'New Password'
        self.fields['new_password1'].widget.attrs['class'] = 'form-control'
        self.fields['new_password1'].widget.attrs['placeholder'] = 'New Password'

        self.fields['new_password2'].label = 'Confirm New Password'
        self.fields['new_password2'].widget.attrs['class'] = 'form-control'
        self.fields['new_password2'].widget.attrs['placeholder'] = 'Confirm New Password'


class UserProfileForm(UserChangeForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Set disabled attribute for uneditable fields
        for field_name in ['username','password', 'created_at',  'is_verified']: 
            self.fields[field_name].disabled = True

        # Add readonly attribute for email field if user is verified
        if self.instance.is_verified:
            self.fields['email'].widget.attrs['readonly'] = True

    username = UsernameField(
        widget=forms.TextInput(attrs={'autofocus': True, 'class': 'form-control', 'placeholder': 'Username or Email'}),
    )

    password = forms.CharField(
        strip=False,
        required=False,
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}),
    )

    # def clean_password(self):
    #     return self.initial.get('password', '')

    # def save(self, commit=True):
    #     instance = super().save(commit=False)
    #     if commit:
    #         fields_changed = []
    #         for field_name, value in self.cleaned_data.items():
    #             if getattr(instance, field_name) != value:
    #                 setattr(instance, field_name, value)
    #                 fields_changed.append(field_name)
    #         instance.save(update_fields=fields_changed)
    #     return instance

    class Meta:
        model = Profile
        fields = ('username', 'first_name', 'last_name', 'email', 'phone_number', 'is_verified', 'avatar', 'created_at' )


class DeleteAccountForm(forms.Form):
    password = forms.CharField(
        label='Enter your password',
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
        required=True
    )



