from django.shortcuts import render
from .my_captcha import FormWithCaptcha

def home(request):
    context = {
        'captcha': FormWithCaptcha,
    }
    return render(request, 'myaccount/login.html', context)
