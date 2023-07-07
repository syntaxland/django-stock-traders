from django.http import HttpResponseRedirect
from django.urls import reverse

import sib_api_v3_sdk
from sib_api_v3_sdk.rest import ApiException

from pprint import pprint
from django.conf import settings

from django.http import HttpResponse
from django.shortcuts import redirect, render, get_object_or_404
from django.contrib import messages
from django.contrib.auth.models import User

from django.utils.crypto import get_random_string
from django.utils import timezone
from datetime import datetime, timedelta

import random, time
from myaccount.models import Profile


# def gen_otp():
#     email_otp = str(random.randint(100000, 999999))
#     return email_otp
# email_otp = gen_otp()

email_otp = str(random.randint(100000, 999999))

def send_email_otp(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')     

        # user = User.objects.get(email=email)
        # user = request.user
        
        # subject = request.POST.get('subject')
        # otp = request.POST.get('otp')
        
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
                <p>Dear { username.title() },</p>
                <p>Thank you for signing up with our service.
                To complete your registration, please use the OTP email_otp provided below:</p><br/>
                <h2>OTP: { email_otp }</h2><br/>
                <p>This email_otp is valid for 15 minutes.</p>
                <p>If you didn't request this verification email, please ignore it.</p>
                <p>Best regards,<br>Softglobal Team</p>
            </body>
            </html>
            """ 
        sender_name = settings.EMAIL_SENDER_NAME
        sender_email = settings.EMAIL_HOST_USER
        sender = {"name":sender_name,"email":sender_email}
        to = [{"email":email,"name":username}]
        send_smtp_email = sib_api_v3_sdk.SendSmtpEmail(to=to, 
                                                        html_content=html_content,
                                                        sender=sender,
                                                        subject=subject) 
        try:
            api_response = api_instance.send_transac_email(send_smtp_email)
            pprint(api_response)

            messages.info(request, 'Email verification email_otp sent to:', email)
            print('Email verification email_otp sent to:', email)

            # Creating a user
            user = User.objects.create(username=username)
            # Save the user, email and OTP to the database
            # Profile.objects.create(user=user, email=email, email_otp=email_otp)
            # HttpResponse('Email verification email_otp sent to your email:', email)

        except ApiException as e:
            print(e)
            # return redirect('verify_email_otp')
            # return Response({'success': 'SMS verification email_otp sent'}, status=status.HTTP_200_OK)
        except Exception as e:
            print(e)
        # verify_email_otp(request, email)
        request.session['email'] = email
        return redirect('verify_email_otp')


    return render(request, 'email_otp_auth/send_email_otp.html')
    # return render(request, 'sms_auth/verfiy_phone.html', {'error': 'Failed to send OTP'})


def verify_email_otp(request):
    if request.method == 'POST':
        otp = request.POST.get('otp')
        email = request.session.get('email')

        email_otp = Profile.objects.filter(
        email_otp=otp, 
        email=email,
        is_verified=False, 
        created_at__gte=timezone.now() - timezone.timedelta(minutes=15)
        ).first()

        try:
            if email_otp:
                email_otp.is_verified = True
                email_otp.save()
                print("Email verification is succussful!")
                return redirect('welcome')
            else:
                print("OTP is wrong or expired!")
        except Exception as e:
            print(e)
            return redirect('verify_email_otp')

    return render(request, 'email_otp_auth/verify_email_otp.html')


def is_otp_expired(request):
    pass

    return redirect('resend_otp')


def resend_otp(request):
    pass
    # if request.method == 'POST':
    #     email = request.POST['email']
    #     try:
        #     email_otp = Profile.objects.get(email=email)
        # except Profile.DoesNotExist:
    #         error = 'Invalid email address'
    #         return render(request, 'resend_otp.html', {'error': error})
    #     else:
    #         if email_otp.is_expired():
    #             email_otp.email_otp = get_random_string(length=6)
    #             send_mail(
    #                 'Verify your email address',
    #                 f'Your verification email_otp is: {email_otp.email_otp}',
    #                 settings.DEFAULT_FROM_EMAIL,
    #                 [email],
    #                 fail_silently=False,
    #             )
    #             email_otp.last_sent_at = timezone.now()
    #             email_otp.save()
    #             return redirect('enter_otp')
    #         else:
    #             error = f'An OTP has already been sent to {email}. \
    #                 Please check your email or wait until it expires.'
    #             return render(request, 'resend_otp.html', {'error': error})
    return render(request, 'email_otp_auth/resend_email_otp.html')
    

def welcome(request, user_id):
    user = User.objects.get(id=user_id)
    # users = User.objects.all()
    user_records = Profile.objects.all()

    context = {
        'user': user
        # 'users':users
    }

    # if context:
    #     return redirect('send_email_otp')
    return render(request, 'email_otp_auth/verified.html', context)


def delete_user(request, user_id):
    user = User.objects.get(id=user_id)
    # users = User.objects.all()
    # user = User.objects.filter(user_id=user_id).first()
    # user = User.objects.filter(user_id=user_id).last()
    # user = get_object_or_404(User, id=user_id)
    user_records = Profile.objects.all()
    delete_user_records = Profile.objects.filter(user=user)
    # if user:
    user.delete()
    # delete_user_records.delete()
    messages.info(request, 'User successfully deleted.')
    time.sleep(10)
    return redirect('send_email_otp')
    # return render(request, 'email_otp_auth/verified.html')
