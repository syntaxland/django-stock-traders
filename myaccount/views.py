from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout as auth_logout, get_user_model
from django.contrib import messages
from django.db.models import Q

from django.contrib.auth.models import User
from .forms import ProfileRegistrationForm, ProfileLoginForm, ForgetPasswordForm
from .models import Profile

from django.contrib.auth.tokens import default_token_generator
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes


## using `UserCreationForm` for user registeration -- checks if username, email, or phone number already exists
##---------------------------------------------------------------------------------------------------
# def register_view(request):
#     form = ProfileRegistrationForm()

#     if request.method == 'POST':
#         form = ProfileRegistrationForm(request.POST)
#         if form.is_valid():
#             # Validate the reCAPTCHA field
#             if form.cleaned_data.get('captcha'):
#                 # Check if the username or email already exists
#                 username = form.cleaned_data['username']
#                 email = form.cleaned_data['email']
#                 phone_number = form.cleaned_data['phone_number']
#                 User = get_user_model()

#                 if User.objects.filter(Q(username=username) | Q(email=email) | Q(phone_number=phone_number)).exists():
#                     # Username, email, or phone number already exists
#                     messages.warning(request, 'User already exists. Hint: username, email, or phone number already exists')
#                 else:
#                     # Create the user
#                     form.save()
#                     messages.success(request, 'Registration successful.')
#                     return redirect('login')
#             else:
#                 # reCAPTCHA validation failed
#                 messages.warning(request, 'Invalid reCAPTCHA. Please try again.')
#         else:
#             # Form validation failed
#             messages.warning(request, 'Invalid form submission. Please correct the errors.')
                
#     return render(request, 'myaccount/register.html', {'form': form})


## using `UserCreationForm` for user registeration (with captcha val)
##---------------------------------------------------------------------------------------------------
# def register_view(request):
#     form = ProfileRegistrationForm()

#     if request.method == 'POST':
#         form = ProfileRegistrationForm(request.POST)
#         if form.is_valid():
#             # Validate the reCAPTCHA field
#             if form.cleaned_data.get('captcha'):
#                 # Create form
#                 form.save()
#                 messages.success(request, 'Form submitted successfully.')
#                 return redirect('login')
#             else:
#                 # reCAPTCHA validation failed
#                 messages.warning(request, 'Invalid reCAPTCHA. Please try again.')
#         else:
#             # Form validation failed
#             messages.info(request, 'Invalid form submission. Please try again.')
                
#     return render(request, 'myaccount/register.html', {'form': form})


### Login with username|email and password for CustomUser model (with captcha val)
##---------------------------------------------------------------------------------------------------
# def login_view(request):
#     form = ProfileLoginForm()

#     if request.method == 'POST':
#         form = ProfileLoginForm(request.POST)
#         if form.is_valid():
#             # Validate the reCAPTCHA field
#             if form.cleaned_data.get('captcha'):
#                 identifier = form.cleaned_data['identifier']
#                 password = form.cleaned_data['password']
#                 User = get_user_model()
#                 try:
#                     user = User.objects.filter(Q(username=identifier) | Q(email=identifier)).first()
#                     user = authenticate(request, username=user.username, password=password)
#                     if user is not None:
#                         login(request, user)
#                         messages.success(request, 'Login successful.')
#                         return redirect('home')
#                     else:
#                         messages.info(request, 'Invalid credentials. Please try again.')
#                 except User.DoesNotExist:
#                     messages.info(request, 'User does not exist.')
#                 except:
#                     messages.warning(request, 'Something went wrong. Please try again.')
#             else:
#                 # reCAPTCHA validation failed
#                 messages.warning(request, 'Invalid reCAPTCHA. Please try again.')
#         else:
#             # Form validation failed
#             messages.info(request, 'Invalid form submission. Please try again.')

#     return render(request, 'myaccount/login.html', {'form': form})


# def login_view(request):
#     form = ProfileLoginForm()

#     if request.method == 'POST':
#         form = ProfileLoginForm(request.POST)
#         if form.is_valid():
#             identifier = form.cleaned_data['identifier']
#             password = form.cleaned_data['password']
#             captcha = form.cleaned_data['captcha']
            
#             # Validate the reCAPTCHA field
#             if captcha:
#                 User = get_user_model()
#                 try:
#                     user = User.objects.filter(Q(username=identifier) | Q(email=identifier)).first()
#                     user = authenticate(request, username=user.username, password=password)
#                     if user is not None:
#                         login(request, user)
#                         messages.success(request, 'Login successful.')
#                         return redirect('home')
#                     else:
#                         form.add_error('identifier', 'Invalid credentials. Please try again.')
#                 except User.DoesNotExist:
#                     form.add_error('identifier', 'User does not exist.')
#                 except:
#                     messages.warning('identifier', 'Invalid credentials. Please try again.')
#             else:
#                 # reCAPTCHA validation failed
#                 form.add_error('captcha', 'Invalid reCAPTCHA. Please try again.')
#         else:
#             # Form validation failed
#             messages.info(request, 'Invalid form submission. Please try again.')

#     return render(request, 'account/login.html', {'form': form})


# # using `UserCreationForm` for user registeration (without captcha)
# #---------------------------------------------------------------------------------------------------
def register_view(request):
    form = ProfileRegistrationForm()

    if request.method == 'POST':
        form = ProfileRegistrationForm(request.POST)
        if form.is_valid():
            # Create form
            form.save()
            messages.success(request, 'Form submitted successfully.')
            return redirect('login')
        else:
            # Form validation failed
            messages.warning(request, 'Invalid form submission. Please try again.')
    return render(request, 'myaccount/register.html', {'form': form})


# Login with username|email and password for CustomUser model (without captcha)
# #---------------------------------------------------------------------------------------------------
def login_view(request):
    form = ProfileLoginForm()

    if request.method == 'POST':
        form = ProfileLoginForm(request.POST)
        if form.is_valid():
            identifier = form.cleaned_data['identifier']
            password = form.cleaned_data['password']
            User = get_user_model()
            try:
                user = User.objects.filter(Q(username=identifier) | Q(email=identifier)).first()
                user = authenticate(request, username=user.username, password=password)
                if user is not None:
                    login(request, user)
                    messages.success(request, 'Login successful.')
                    return redirect('home')
                else:
                    messages.info(request, 'Invalid credentials. Please try again.')
            except User.DoesNotExist:
                messages.info(request, 'User does not exist.')
            except:
                messages.warning(request, 'Something went wrong. Please try again.')
        else:
            # Form validation failed
            messages.info(request, 'Invalid form submission. Please try again.')

    return render(request, 'myaccount/login.html', {'form': form})


# using `forms.ModelForm` for user registeration
#---------------------------------------------------------------------------------------------------
# def register_view(request):
#     form = ProfileRegistrationForm()

#     if request.method == 'POST':
#         form = ProfileRegistrationForm(request.POST)
#         if form.is_valid():
#             email = form.cleaned_data['email']
#             password = form.cleaned_data['password1']
#             User = get_user_model()
#             user = User.objects.create_user(email=email, password=password)
#             # Set additional form fields
#             user.username = form.cleaned_data['username']
#             user.first_name = form.cleaned_data['first_name']
#             user.last_name = form.cleaned_data['last_name']
#             user.phone_number = form.cleaned_data['phone_number']
#             user.save()

#             messages.success(request, 'Form submitted successfully.')
#             return redirect('login')
#         else:
#             messages.warning(request, 'Invalid form submission. Please try again.')
    
#     return render(request, 'myaccount/register.html', {'form': form})


# Login with username and password (CustomUser model)
#---------------------------------------------------------------------------------------------------
# def login_view(request):
#     if request.method == 'POST':
#         form = ProfileLoginForm(request.POST)
#         if form.is_valid():
#             username = form.cleaned_data['username']
#             password = form.cleaned_data['password']
#             User = get_user_model()
#             try:
#                 user = User.objects.get(username=username)
#                 user = authenticate(request, username=username, password=password)
#                 if user is not None:
#                     login(request, user)
#                     messages.success(request, 'Login successful.')
#                     return redirect('home')
#                 else:
#                     messages.error(request, 'Invalid credentials. Please try again.')
#             except User.DoesNotExist:
#                 messages.error(request, 'User does not exist.')
#         else:
#             # Form validation failed
#             messages.error(request, 'Invalid form submission. Please try again.')
#     else:
#         form = ProfileLoginForm()
#     return render(request, 'myaccount/login.html', {'form': form})



# Login with email and password (CustomUser model)
#---------------------------------------------------------------------------------------------------
# def login_view(request):
#     if request.method == 'POST':
#         form = ProfileLoginForm(request.POST)
#         if form.is_valid():
#             email = form.cleaned_data['email']
#             password = form.cleaned_data['password']
#             User = get_user_model()
#             try:
#                 user = User.objects.get(email=email)
#                 username = user.username
#                 user = authenticate(request, username=username, password=password)
#                 if user is not None:
#                     login(request, user)
#                     messages.success(request, 'Login successful.')
#                     print('User:', user, request.user.first_name, request.user.email, request.user.phone_number)
#                     print('User is authenticated:', request.user.is_authenticated)
#                     return redirect('homepage')
#             except User.DoesNotExist:
#                 messages.error(request, 'User does not exist. Please try again.')
#             messages.error(request, 'Invalid credentials. Please try again.')
#     else:
#         form = ProfileLoginForm()
#     return render(request, 'myaccount/login.html', {'form': form})


@login_required(login_url='login')
def logout_view(request):
    auth_logout(request)
    return redirect('login')


def forget_password(request):
    form = ForgetPasswordForm()

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
    
    return render(request, 'myaccount/forget_password.html', {'form': form})


def send_email_otp(request):
    ...


def send_sms_otp(request):
    pass

@login_required(login_url='login')
def home(request):
    return render(request, 'base.html')


@login_required(login_url='login')
def profile(request):
    pass
    return render(request, 'myaccount/profile.html')
