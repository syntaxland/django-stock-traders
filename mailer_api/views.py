# from django.http import HttpResponseRedirect

# import sib_api_v3_sdk
# from sib_api_v3_sdk.rest import ApiException

# from pprint import pprint
# from django.conf import settings 

# from django.http import HttpResponse
# from django.shortcuts import redirect, render, get_object_or_404
# from django.contrib import messages
# from django.contrib.auth.models import User

# from django.utils.crypto import get_random_string
# from django.utils import timezone
# from datetime import datetime, timedelta
# import random
# import time

# from .models import EmailVerification

# from rest_framework import status
# from rest_framework.response import Response

# from django.urls import reverse
# from django.utils.timezone import now
# import uuid

# # import base64
# # import random
# # import string

# # def generate_verification_link(email):
# #     token = ''.join(random.choices(string.ascii_letters + string.digits, k=32))
# #     encoded_email = base64.urlsafe_b64encode(email.encode()).decode()
# #     verification_link = f'http://syntaxland.com/verify-email/{encoded_email}/{token}/'
# #     return verification_link

# # verification_url = generate_verification_link('jb@ok.com')
# # print('\nHi, your email activation link is:\n\n', verification_url)


# # def generate_token():
# #     token = uuid.uuid4()
# #     return token

# # def generate_token():
# #     return uuid.uuid4()

# # Generate token
# token = uuid.uuid4()

# def signup(request):
#     # Getting user request
#     if request.method == 'POST':
#         username = request.POST.get('username')
#         email = request.POST.get('email')

#         # Saving email to session
#         request.session['email'] = email
#         request.session['username'] = username

#         user = User.objects.create_user(username=username, email=email)
#         email_verification = EmailVerification.objects.create(user=user, email=email, token=token)

#         # email_verification.generate_token()
#         email_verification.save()

#         # Using reverse method to dynamically sent tokenize links
#         verification_link = request.build_absolute_uri(reverse('verify_email', args=[str(email_verification.token)]))
#         return send_verification_email(request, username, email, verification_link)
#         # verification_link = f"{request.scheme}://{request.get_host()}/verify-email/{email_verification.token}"
#     else:
#         return render(request, 'email_link_auth/signup.html')


# def send_verification_email(request, username, email, verification_link):
#     # email = request.POST['email']
#     # username = request.POST['username']

#     # Email Sending API Config
#     configuration = sib_api_v3_sdk.Configuration()
#     configuration.api_key['api-key'] = settings.SENDINBLUE_API_KEY
#     api_instance = sib_api_v3_sdk.TransactionalEmailsApi(sib_api_v3_sdk.ApiClient(configuration))
#     # Sending email
#     subject = "Email Verification"
#     html_content = f"""
#     <!DOCTYPE html>
#         <html>
#         <head>
#             <title>Email Verification</title>
#         </head>
#         <body>
#             <p>Dear { username.title() },</p>
#             <p>Thank you for signing up for our service. To complete your registration, 
#                 please click the button below to verify your email address:</p>

#              <!--<p><a href="{ verification_link }"></a></p>-->

#             <p><a href="{ verification_link }" style="display: inline-block; 
#                 background-color: #2196f3; color: #fff; padding: 10px 20px; 
#                 text-decoration: none;">Verify Email Address</a></p>

#             <p>This link is valid for 15 minutes.
#             If you didn't request this verification email, please ignore it.</p>
#             <p>Best regards,<br>Softglobal Team</p>
#         </body>
#         </html>
#         """
#     sender_name = settings.EMAIL_SENDER_NAME
#     sender_email = settings.EMAIL_HOST_USER
#     sender = {"name":sender_name,"email":sender_email}
#     to = [{"email":email,"name":username}]
#     send_smtp_email = sib_api_v3_sdk.SendSmtpEmail(to=to, 
#                                                     html_content=html_content,
#                                                     sender=sender,
#                                                     subject=subject) 
#     try:
#         api_response = api_instance.send_transac_email(send_smtp_email)
#         pprint(api_response)
#     except ApiException as e:
#         print(e)
#         return redirect('signup')
#     except Exception as e:
#         print(e)
#         return messages.error(request, 'Something went wrong.')
#     messages.success(request, 'A verification email has been sent. Please check your inbox.')
#     print('Email verification link sent to:', email)
#     # resend_verification(request, username, email, verification_link)
#     time.sleep(5)
#     return redirect('login')


# def resend_verification(request):
#     if request.method == 'POST':
#         # email = request.POST['email']

#         # request.session['email'] = email
#         username = request.session['username']  
#         email = request.session['email']  

#         # token = uuid.uuid4()

#         try:
#             email_verification = EmailVerification.objects.get(email=email)
#         except EmailVerification.DoesNotExist:
#             messages.error(request, 'No verification email was sent to this email.')
#             return redirect('signup')

#         if email_verification.verified:
#             messages.warning(request, 'This email has already been verified.')
#             return redirect('welcome')
        
#         if (timezone.now() - email_verification.created_at).total_seconds() > 900:
#             email_verification.token
#             # email_verification.generate_token()
#             email_verification.save()
#             verification_link = request.build_absolute_uri(reverse('verify_email', args=[str(email_verification.token)]))
#             # send_verification_email(email, verification_link)


#             configuration = sib_api_v3_sdk.Configuration()
#             configuration.api_key['api-key'] = settings.SENDINBLUE_API_KEY
#             api_instance = sib_api_v3_sdk.TransactionalEmailsApi(sib_api_v3_sdk.ApiClient(configuration))
#             # Sending email
#             subject = "Email Verification"
#             html_content = f"""
#             <!DOCTYPE html>
#                 <html>
#                 <head>
#                     <title>Email Verification</title>
#                 </head>
#                 <body>
#                     <p>Dear { username.title() },</p>
#                     <p>Thank you for signing up for our service. To complete your registration, 
#                         please click the button below to verify your email address:</p>
#                     <p><a href="{ verification_link }" style="display: inline-block; 
#                         background-color: #2196f3; color: #fff; padding: 10px 20px; 
#                         text-decoration: none;">Verify Email Address</a>
#                     </p>
#                     <p>This code is valid for 15 minutes.
#                     If you didn't request this verification email, please ignore it.</p>
#                     <p>Best regards,<br>Softglobal Team</p>
#                 </body>
#                 </html>
#                 """
            
#             sender_name = settings.EMAIL_SENDER_NAME
#             sender_email = settings.EMAIL_HOST_USER
#             sender = {"name":sender_name,"email":sender_email}
#             to = [{"email":email,"name":username}]
#             send_smtp_email = sib_api_v3_sdk.SendSmtpEmail(to=to, 
#                                                             html_content=html_content,
#                                                             sender=sender,
#                                                             subject=subject) 
#             try:
#                 api_response = api_instance.send_transac_email(send_smtp_email)
#                 pprint(api_response)

#                 messages.success(request, 'A verification email has been sent. Please check your inbox.')
#                 print('Email verification link sent to:', email)
#                 return redirect('login')
#             except ApiException as e:
#                 print(e)
#                 return redirect('resend_verification')
#             except Exception as e:
#                 print(e)
#             # verify_email_otp(request, email)


#             messages.success(request, 'A new verification email has been sent. Please check your inbox.')
#             return redirect('login')
#         else:
#             messages.warning(request, 'Please wait at least 15 minutes before requesting a new verification email.')
#             return redirect('resend_verification')
#     else:
#         return render(request, 'email_link_auth/resend_verification.html')


# def verify_email(request, token):
#     email_verification = EmailVerification.objects.filter(token=token).first()
#     if email_verification:
#         if not email_verification.verified:
#             email_verification.verified = True
#             email_verification.save()
#             messages.success(request, 'Email address has been verified successfully. You can now log in.')
#             return redirect('login')
#         else:
#             messages.warning(request, 'Email address has already been verified.')
#             return redirect('login')
#     else:
#         messages.warning(request, 'Invalid verification link.')
#         return redirect('login')

# def welcome(request):
#     # context = {'user_id': user_id}
#     # if context:
#     #     return redirect('send_email_otp')
#     return render(request, 'email_link_auth/verified.html')

# def login(request):
#     return render(request, 'email_link_auth/login.html')


