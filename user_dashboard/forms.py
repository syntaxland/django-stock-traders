# from django import forms
# from . models import TraderData 

# class TraderDataForm(forms.ModelForm):
#     class Meta:
#         model = TraderData
#         fields = ['trader', 'amount]
#         widgets = {
#             'category': forms.TextInput(attrs={'class': 'form-control'}),
#             'num_of_products': forms.TextInput(attrs={'class': 'form-control'}),
#         }


from django import forms

class TraderForm(forms.Form):
    trader = forms.CharField(label='Trader Name', max_length=100)
    amount = forms.DecimalField(label='Initial Amount', max_digits=10, decimal_places=2)
