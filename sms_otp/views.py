from django.http import HttpResponse
from django.shortcuts import redirect, render, get_object_or_404
from django.contrib import messages

from django.utils.crypto import get_random_string
from django.utils import timezone
from datetime import datetime, timedelta

import random
from .models import SmsOtp
from twilio.rest import Client
from django.conf import settings

from rest_framework import status
from rest_framework.response import Response

code = str(random.randint(100000, 999999))

def send_sms_otp(request):
    account_sid = settings.TWILIO_ACCOUNT_SID 
    auth_token = settings.TWILIO_AUTH_TOKEN 
    client = Client(account_sid, auth_token)

    if request.method == 'POST':
        phone = request.POST.get('phone')
        
        try:
            message = client.messages.create(
                    body=f'OTP: {code}',
                    from_=settings.TWILIO_PHONE_NUMBER,
                    to=phone
                )
            print(message.sid)
            print('SMS verification code sent to:', phone)
            messages.info(request, 'SMS verification code sent to:', phone)


            # Save the OTP to the database
            SmsOtp.objects.create(phone=phone, code=code)

            return redirect('verify_sms_otp', phone=phone)
            # return Response({'success': 'SMS verification code sent'}, status=status.HTTP_200_OK)
        except Exception as e:
            print(e)
            return redirect('send_sms_otp')
        
    return render(request, 'sms_auth/verfiy_phone.html')
    # return render(request, 'sms_auth/verfiy_phone.html', {'error': 'Failed to send OTP'})



def verify_sms_otp(request, phone):
    if request.method == 'POST':
        otp = request.POST.get('otp')
        try:
            sms_otp = SmsOtp.objects.get(phone=phone)
        except SmsOtp.DoesNotExist:
            return render(request, 'verify_sms_otp.html', {'error': 'OTP expired or invalid'})

        if sms_otp.code == otp and not sms_otp.is_verified and sms_otp.created_at + timedelta(minutes=15) > datetime.now():
            sms_otp.is_verified = True
            sms_otp.save()
            return redirect('welcome')
        else:
            return render(request, 'verify_sms_otp.html', {'error': 'OTP expired or invalid'})
    else:
        return render(request, 'verify_sms_otp.html')
    
    
# def verify_sms_otp(request, phone):
    
#     if request.method == 'POST':
#         otp = request.POST['otp']

#         sms_otp = SmsOtp.objects.filter(
#             phone=phone,
#             code=otp,
#             is_verified=False,
#             created_at__gte=timezone.now() - timezone.timedelta(minutes=15)
#         ).first()

#         if sms_otp:
#             sms_otp.is_verified = True
#             sms_otp.save()
#             return redirect('welcome')
#         else:
#             return render(request, 'verify_sms_otp.html', {'error': 'OTP expired or invalid'})

#     return render(request, 'verify_sms_otp.html')

        # sms_otp = get_object_or_404(SmsOtp, phone=phone)
        # if SmsOtp.code==otp:
        #     sms_otp.delete()
        #     # context = {'phone': phone}
        #     print("Your phone number is verifed with OTP: ", otp)
        #     print(HttpResponse('OTP verification successful'))
        #     return redirect('welcome')
            
#         # return render(request, 'sms_auth/verify_sms_otp.html', {'phone': phone})
        
#         # Retrieve the SmsOtp instance with the corresponding phone value
#         # sms_otp = get_object_or_404(SmsOtp, phone=phone)
#         sms_otp = SmsOtp.objects.filter(phone=phone, code=otp).first()

#         if sms_otp.code==otp:
            
#             sms_otp.delete()
#             phone.is_verified = True

#             print("Your phone number", phone, "is verifed with OTP: ", otp)
#             print(HttpResponse('OTP verification successful'))
#             # return render(request, 'sms_auth/verify_sms_otp.html', {'phone': phone})
#             return redirect('welcome', phone=phone)
#         # else:
#         #     return render(request, 'sms_auth/verify_sms_otp.html', {'error': 'Incorrect OTP'}, {'phone': phone})
    
    # return render(request, 'sms_auth/verify_sms_otp.html', {'phone': phone})


def welcome(request):
    return render(request, 'sms_auth/verified.html')


