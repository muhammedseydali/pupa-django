from django import forms
from .models import Order

class OrderCreateForm(forms.ModelForm):

    PAYMENT_METHOD_CHOICES = (
        ('Razorapy', 'Razorapy'),
        ('COD', 'COD')
    )

    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your Name'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Your Email'}))
    phone = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your Phone Number'}))
    address = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Shipping Address'}))
    account_no = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Account Number'}))
    transaction_id = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Transaction ID'}))
    payment_method = forms.ChoiceField(choices=PAYMENT_METHOD_CHOICES, widget=forms.RadioSelect(attrs={'class': 'form-check-input'}))

    class Meta:
        model = Order
        fields = ['name', 'email', 'phone', 'address', 'payment_method', 'account_no', 'transaction_id']
