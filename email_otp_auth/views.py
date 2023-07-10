from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import EmailOTPVerificationForm
from .models import EmailOtp
from django.conf import settings

import sib_api_v3_sdk
from sib_api_v3_sdk.rest import ApiException

from django.contrib.auth import get_user_model

User = get_user_model()


@login_required
def send_email_otp(request):
    user = request.user

    email_otp, created = EmailOtp.objects.get_or_create()
    email_otp.generate_email_otp()

    # Email Sending API Config
    configuration = sib_api_v3_sdk.Configuration()
    configuration.api_key['api-key'] = settings.SENDINBLUE_API_KEY
    api_instance = sib_api_v3_sdk.TransactionalEmailsApi(sib_api_v3_sdk.ApiClient(configuration))

    # Sending email
    subject = "OTP Email Verification"
    html_content = f"""
        <!DOCTYPE html>
        <html>
        <head>
            <title>OTP Email Verification</title>
        </head>
        <body>
            <p>Dear {user.username.title()},</p>
            <p>Thank you for signing up with our service.
            To complete your registration, please use the OTP provided below:</p><br/>
            <h2>OTP: {email_otp.email_otp}</h2><br/>
            <p>This OTP is valid for 15 minutes.</p>
            <p>If you didn't request this verification email, please ignore it.</p>
            <p>Best regards,<br>Softglobal Team</p>
        </body>
        </html>
    """
    sender_name = settings.EMAIL_SENDER_NAME
    sender_email = settings.EMAIL_HOST_USER
    sender = {"name": sender_name, "email": sender_email}
    to = [{"email": user.email, "name": user.username}]
    send_smtp_email = sib_api_v3_sdk.SendSmtpEmail(
        to=to,
        html_content=html_content,
        sender=sender,
        subject=subject
    )

    try:
        api_response = api_instance.send_transac_email(send_smtp_email)
        messages.success(request, f'Email verification OTP sent to: {user.email}')
    except ApiException as e:
        print(e)
        messages.warning(request, 'Failed to send verification email.')

    return redirect('verify_email_otp')


@login_required
def verify_email_otp(request):
    form = EmailOTPVerificationForm()

    if request.method == 'POST':
        form = EmailOTPVerificationForm(request.POST)

        if form.is_valid():
            otp = form.cleaned_data['otp']
            email_otp = EmailOtp.objects.filter(email_otp=otp).first()

            if email_otp and email_otp.is_valid():
                email_otp.delete()
                user = User.objects.get(pk=request.user.pk)
                user.is_verified = True  # Update the is_verified field on the User model
                user.save()
                messages.success(request, 'Email verification successful!')
                return redirect('profile')
            else:
                messages.warning(request, 'Invalid or expired OTP. Please try again.')

    return render(request, 'myaccount/verify_email_otp.html', {'form': form})


@login_required
def resend_email_otp(request):
    user = request.user

    email_otp, created = EmailOtp.objects.get_or_create()
    email_otp.generate_email_otp()

    # Email Sending API Config
    configuration = sib_api_v3_sdk.Configuration()
    configuration.api_key['api-key'] = settings.SENDINBLUE_API_KEY
    api_instance = sib_api_v3_sdk.TransactionalEmailsApi(sib_api_v3_sdk.ApiClient(configuration))

    # Sending email
    subject = "OTP Email Verification"
    html_content = f"""
        <!DOCTYPE html>
        <html>
        <head>
            <title>OTP Email Verification</title>
        </head>
        <body>
            <p>Dear {user.username.title()},</p>
            <p>Thank you for signing up with our service.
            To complete your registration, please use the OTP provided below:</p><br/>
            <h2>OTP: {email_otp.email_otp}</h2><br/>
            <p>This OTP is valid for 15 minutes.</p>
            <p>If you didn't request this verification email, please ignore it.</p>
            <p>Best regards,<br>Softglobal Team</p>
        </body>
        </html>
    """
    sender_name = settings.EMAIL_SENDER_NAME
    sender_email = settings.EMAIL_HOST_USER
    sender = {"name": sender_name, "email": sender_email}
    to = [{"email": user.email, "name": user.username}]
    send_smtp_email = sib_api_v3_sdk.SendSmtpEmail(
        to=to,
        html_content=html_content,
        sender=sender,
        subject=subject
    )

    try:
        api_response = api_instance.send_transac_email(send_smtp_email)
        messages.success(request, f'Email verification OTP resent.')
    except ApiException as e:
        print(e)
        messages.warning(request, 'Failed to send verification email.')

    return redirect('verify_email_otp')


# from django.shortcuts import render, redirect
# from django.contrib.auth.decorators import login_required
# from django.contrib import messages
# from .forms import EmailOTPVerificationForm
# from .models import EmailOtp
# from django.conf import settings

# import sib_api_v3_sdk
# from sib_api_v3_sdk.rest import ApiException

# from django.contrib.auth import get_user_model

# User = get_user_model()


# @login_required
# def send_email_otp(request):
#     user = request.user

#     email_otp, created = EmailOtp.objects.get_or_create(user=user)
#     email_otp.generate_email_otp()

#     # Email Sending API Config
#     configuration = sib_api_v3_sdk.Configuration()
#     configuration.api_key['api-key'] = settings.SENDINBLUE_API_KEY
#     api_instance = sib_api_v3_sdk.TransactionalEmailsApi(sib_api_v3_sdk.ApiClient(configuration))

#     # Sending email
#     subject = "OTP Email Verification"
#     html_content = f"""
#         <!DOCTYPE html>
#         <html>
#         <head>
#             <title>OTP Email Verification</title>
#         </head>
#         <body>
#             <p>Dear {user.username.title()},</p>
#             <p>Thank you for signing up with our service.
#             To complete your registration, please use the OTP provided below:</p><br/>
#             <h2>OTP: {email_otp.email_otp}</h2><br/>
#             <p>This OTP is valid for 15 minutes.</p>
#             <p>If you didn't request this verification email, please ignore it.</p>
#             <p>Best regards,<br>Softglobal Team</p>
#         </body>
#         </html>
#     """
#     sender_name = settings.EMAIL_SENDER_NAME
#     sender_email = settings.EMAIL_HOST_USER
#     sender = {"name": sender_name, "email": sender_email}
#     to = [{"email": user.email, "name": user.username}]
#     send_smtp_email = sib_api_v3_sdk.SendSmtpEmail(
#         to=to,
#         html_content=html_content,
#         sender=sender,
#         subject=subject
#     )

#     try:
#         api_response = api_instance.send_transac_email(send_smtp_email)
#         messages.success(request, f'Email verification OTP sent to: {user.email}')
#     except ApiException as e:
#         print(e)
#         messages.warning(request, 'Failed to send verification email.')

#     return redirect('verify_email_otp')


# @login_required
# def verify_email_otp(request):
#     form = EmailOTPVerificationForm()

#     if request.method == 'POST':
#         form = EmailOTPVerificationForm(request.POST)

#         if form.is_valid():
#             otp = form.cleaned_data['otp']
#             email_otp = EmailOtp.objects.filter(user=request.user).first()
#             print(email_otp)
#             print(email_otp.is_valid())
#             print(email_otp.email_otp)
#             print(str(email_otp.email_otp)) 

#             if email_otp and email_otp.is_valid() and str(email_otp.email_otp) == otp:
#                 email_otp.delete()
#                 user = User.objects.get(pk=request.user.pk)
#                 user.is_verified = True  # Update the is_verified field on the User model
#                 user.save()
#                 messages.success(request, 'Email verification successful!')
#                 return redirect('profile')
#             else:
#                 messages.warning(request, 'Invalid or expired OTP. Please try again.')

#     return render(request, 'myaccount/verify_email_otp.html', {'form': form})


# @login_required
# def resend_email_otp(request):
#     user = request.user

#     email_otp, created = EmailOtp.objects.get_or_create(user=user)

#     if email_otp and email_otp.is_valid():
#         messages.warning(request, 'An active OTP already exists. Please wait before requesting a new one.')
#     else:
#         email_otp.generate_email_otp()

#         # Email Sending API Config
#         configuration = sib_api_v3_sdk.Configuration()
#         configuration.api_key['api-key'] = settings.SENDINBLUE_API_KEY
#         api_instance = sib_api_v3_sdk.TransactionalEmailsApi(sib_api_v3_sdk.ApiClient(configuration))

#         # Sending email
#         subject = "OTP Email Verification"
#         html_content = f"""
#             <!DOCTYPE html>
#             <html>
#             <head>
#                 <title>OTP Email Verification</title>
#             </head>
#             <body>
#                 <p>Dear {user.username.title()},</p>
#                 <p>Thank you for signing up with our service.
#                 To complete your registration, please use the OTP provided below:</p><br/>
#                 <h2>OTP: {email_otp.email_otp}</h2><br/>
#                 <p>This OTP is valid for 15 minutes.</p>
#                 <p>If you didn't request this verification email, please ignore it.</p>
#                 <p>Best regards,<br>Softglobal Team</p>
#             </body>
#             </html>
#         """
#         sender_name = settings.EMAIL_SENDER_NAME
#         sender_email = settings.EMAIL_HOST_USER
#         sender = {"name": sender_name, "email": sender_email}
#         to = [{"email": user.email, "name": user.username}]
#         send_smtp_email = sib_api_v3_sdk.SendSmtpEmail(
#             to=to,
#             html_content=html_content,
#             sender=sender,
#             subject=subject
#         )

#         try:
#             api_response = api_instance.send_transac_email(send_smtp_email)
#             messages.success(request, f'Email verification OTP resent.')
#         except ApiException as e:
#             print(e)
#             messages.warning(request, 'Failed to send verification email.')

#     return redirect('verify_email_otp')





# from django.shortcuts import render, redirect
# from django.contrib.auth.decorators import login_required
# from django.contrib.auth import get_user_model
# from django.contrib import messages
# from .forms import EmailOTPVerificationForm
# from .models import EmailOtp
# from django.conf import settings
# import sib_api_v3_sdk
# from sib_api_v3_sdk.rest import ApiException
# from django.template.loader import render_to_string
# from django.core.mail import send_mail

# User = get_user_model()


# @login_required
# def send_email_otp(request):
#     user = request.user

#     email_otp, created = EmailOtp.objects.get_or_create(user=user)
#     email_otp.generate_email_otp()

#     subject = "OTP Email Verification"
#     html_message = render_to_string('myaccount/email_otp_verification.html', {'user': user, 'otp': email_otp.email_otp})
#     from_email = settings.DEFAULT_FROM_EMAIL
#     recipient_list = [user.email]

#     try:
#         send_mail(subject, '', from_email, recipient_list, html_message=html_message)
#         messages.success(request, f'Email verification OTP sent to: {user.email}')
#     except Exception as e:
#         print(e)
#         messages.warning(request, 'Failed to send verification email.')

#     return redirect('verify_email_otp')


# @login_required
# def verify_email_otp(request):
#     form = EmailOTPVerificationForm()

#     if request.method == 'POST':
#         form = EmailOTPVerificationForm(request.POST)

#         if form.is_valid():
#             otp = form.cleaned_data['otp']
#             email_otp = EmailOtp.objects.filter(user=request.user).first()

#             if email_otp and email_otp.is_valid() and email_otp.email_otp == otp:
#                 email_otp.delete()
#                 user = User.objects.get(pk=request.user.pk)
#                 user.is_verified = True  # Update the is_verified field on the User model
#                 user.save()
#                 messages.success(request, 'Email verification successful!')
#                 return redirect('profile')
#             else:
#                 messages.warning(request, 'Invalid or expired OTP. Please try again.')

#     return render(request, 'myaccount/verify_email_otp.html', {'form': form})


# @login_required
# def resend_email_otp(request):
#     user = request.user

#     email_otp, created = EmailOtp.objects.get_or_create(user=user)

#     if email_otp and email_otp.is_valid():
#         messages.warning(request, 'An active OTP already exists. Please wait before requesting a new one.')
#     else:
#         email_otp.generate_email_otp()

#         subject = "OTP Email Verification"
#         html_message = render_to_string('myaccount/email_otp_verification.html', {'user': user, 'otp': email_otp.email_otp})
#         from_email = settings.DEFAULT_FROM_EMAIL
#         recipient_list = [user.email]

#         try:
#             send_mail(subject, '', from_email, recipient_list, html_message=html_message)
#             messages.success(request, f'Email verification OTP resent.')
#         except Exception as e:
#             print(e)
#             messages.warning(request, 'Failed to send verification email.')

#     return redirect('verify_email_otp')

