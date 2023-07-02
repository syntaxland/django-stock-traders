from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout as auth_logout
from .forms import ProfileRegistrationForm, ProfileLoginForm, ForgetPasswordForm
from django.contrib import messages

from django.contrib.auth.models import User
from django.contrib.auth.tokens import default_token_generator
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout as auth_logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

# def register(request):
#     if request.method == 'POST':
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             # Validate the reCAPTCHA field
#             if form.cleaned_data.get('captcha'):
#                 # Create a new user
#                 form.save()
#                 # Log in the user
#                 username = form.cleaned_data.get('username')
#                 password = form.cleaned_data.get('password1')
#                 user = authenticate(request, username=username, password=password)
#                 if user is not None:
#                     login(request, user)
#                     # Redirect to the dashboard or another page
#                     return redirect('dashboard')
#             else:
#                 # reCAPTCHA validation failed
#                 messages.error(request, 'Invalid reCAPTCHA. Please try again.')
#         else:
#             # Form validation failed
#             messages.error(request, 'Invalid form submission. Please try again.')
#     else:
#         form = UserCreationForm()
#     return render(request, 'myaccount/register.html', {'form': form})


# def register(request):
#     if request.method == 'POST':
#         form = ProfileRegistrationForm(request.POST)
#         if form.is_valid():
#             # Validate the reCAPTCHA field
#             if form.cleaned_data.get('captcha'):
#                 # Create a user object
#                 user = form.save()
#                 # Log in the user
#                 login(request, user)
#                 # Redirect to the dashboard or another page
#                 return redirect('dashboard')
#             else:
#                 # reCAPTCHA validation failed
#                 messages.error(request, 'Invalid reCAPTCHA. Please try again.')
#         else:
#             # Form validation failed
#             messages.error(request, 'Invalid form submission. Please try again.')
#     else:
#         form = ProfileRegistrationForm()
#     return render(request, 'myaccount/register.html', {'form': form})


# def user_login(request):
#     if request.method == 'POST':
#         form = ProfileLoginForm(request.POST)
#         if form.is_valid():
#             # Validate the reCAPTCHA field
#             if form.cleaned_data.get('captcha'):
#                 # reCAPTCHA validation passed
#                 email = form.cleaned_data['email']
#                 password = form.cleaned_data['password']
#                 user = authenticate(request, email=email, password=password)
#                 if user is not None:
#                     login(request, user)
#                     return redirect('dashboard')
#                 else:
#                     # Authentication failed
#                     messages.error(request, 'Invalid email or password. Please try again.')
#             else:
#                 # reCAPTCHA validation failed
#                 messages.error(request, 'Invalid reCAPTCHA. Please try again.')
#         else:
#             # Form validation failed
#             messages.error(request, 'Invalid form submission. Please try again.')
#     else:
#         form = ProfileLoginForm()
#     return render(request, 'myaccount/login.html', {'form': form})


def register(request):
    if request.method == 'POST':
        form = ProfileRegistrationForm(request.POST)
        if form.is_valid():
            # Validate the reCAPTCHA field
            if form.cleaned_data.get('captcha'):
                # Create a user object
                user = User.objects.create_user(
                    username=form.cleaned_data['username'],
                    email=form.cleaned_data['email'],
                    password=form.cleaned_data['password']
                )
                # Associate the user with the profile
                profile = form.save(commit=False)
                profile.user = user
                profile.username = form.cleaned_data['username']
                profile.first_name = form.cleaned_data['first_name']
                profile.last_name = form.cleaned_data['last_name']
                profile.phone_number = form.cleaned_data['phone_number']
                profile.save()
                # Log in the user
                login(request, user)
                # Redirect to the dashboard or another page
                return redirect('dashboard')
            else:
                # reCAPTCHA validation failed
                messages.error(request, 'Invalid reCAPTCHA. Please try again.')
        else:
            # Form validation failed
            messages.error(request, 'Invalid form submission. Please try again.')
    else:
        form = ProfileRegistrationForm()
    return render(request, 'myaccount/register.html', {'form': form})


def user_login(request):
    if request.method == 'POST':
        form = ProfileLoginForm(request.POST)
        if form.is_valid():
            # Validate the reCAPTCHA field
            if form.cleaned_data.get('captcha'):
                # reCAPTCHA validation passed
                    email = form.cleaned_data['email']
                    password = form.cleaned_data['password']
                    user = authenticate(request, email=email, password=password)
                    print('user:', user)
                    print('user.is_authenticated:', request.user.is_authenticated)  
                    if user is not None:
                        login(request, user)
                    return redirect('dashboard')
            else:
                # reCAPTCHA validation failed
                messages.error(request, 'Invalid reCAPTCHA. Please try again.')
        else:
            # Form validation failed
            messages.error(request, 'Invalid form submission. Please try again.')
    else:
        form = ProfileLoginForm()
    return render(request, 'myaccount/login.html', {'form': form})


@login_required(login_url='login')
def user_logout(request):
    auth_logout(request)
    return redirect('login')


def forget_password(request):
    if request.method == 'POST':
        pass
#         form = ForgetPasswordForm(request.POST)
#         if form.is_valid():
#             email = form.cleaned_data['email']
            
#             # Check if the user with the provided email exists
#             try:
#                 user = User.objects.get(email=email)
#             except User.DoesNotExist:
#                 user = None
            
#             if user is not None:
#                 # Generate the password reset token
#                 token_generator = default_token_generator
#                 uid = urlsafe_base64_encode(force_bytes(user.pk))
#                 token = token_generator.make_token(user)
                
#                 # Build the reset password URL
#                 current_site = get_current_site(request)
#                 reset_password_url = f"http://{current_site.domain}/reset-password/{uid}/{token}/"
                
#                 # Create the email subject and message
#                 subject = 'Reset Your Password'
#                 message = render_to_string('myaccount/reset_password_email.html', {
#                     'user': user,
#                     'reset_password_url': reset_password_url,
#                 })
                
#                 # Send the password reset email
#                 send_mail(subject, message, 'noreply@example.com', [email])
                
#                 # Display a success message
#                 messages.success(request, 'An email has been sent with instructions to reset your password.')
                
#                 return redirect('login')
#             else:
#                 # Display an error message if the email is not associated with any user
#                 messages.error(request, 'Invalid email address.')
#     else:
#         form = ForgetPasswordForm()
    
#     return render(request, 'myaccount/forget_password.html', {'form': form})


def send_email_otp(request):
    ...


def send_sms_otp(request):
    pass


def home(request):
    return render(request, 'home.html')
