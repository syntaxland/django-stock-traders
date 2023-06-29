from django import forms
from .models import TraderData

class TraderForm(forms.ModelForm):
    trader = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={'placeholder': 'Trader Name'})
    )
    amount = forms.DecimalField(
        max_digits=10,
        decimal_places=2,
        widget=forms.TextInput(attrs={'placeholder': 'Default Amount = 100 USD'})
    )

    class Meta:
        model = TraderData
        fields = ['trader', 'amount']
