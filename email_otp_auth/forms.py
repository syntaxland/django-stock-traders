from django import forms


class EmailOTPVerificationForm(forms.Form):
    otp = forms.CharField(
        label='Enter the OTP sent to your email address', 
        max_length=6, widget=forms.TextInput(attrs={'class': 'form-control'})
        )


class ResendOTPForm(forms.Form):
    pass
