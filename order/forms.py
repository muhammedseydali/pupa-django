from django import forms
from .models import Order

class OrderCreateForm(forms.ModelForm):
    DIVISION_CHOICES = (
        ('Dhaka', 'Dhaka'),
        ('Chattagram', 'Chattagram'),
        ('Rajshahi', 'Rajshahi '),
    )

    DISTRICT_CHOICES = (
        ('Dhaka', 'Dhaka'), 
        ('Gazipur', 'Gazipur'),
        ('Narayanganj', 'Narayanganj'),
    )

    PAYMENT_METHOD_CHOICES = (
        ('Rocket', 'Rocket'),
        ('Bkash', 'Bkash')
    )

    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your Name'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Your Email'}))
    phone = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your Phone Number'}))
    address = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Shipping Address'}))
    division = forms.ChoiceField(choices=DIVISION_CHOICES, widget=forms.Select(attrs={'class': 'form-control'}))
    district = forms.ChoiceField(choices=DISTRICT_CHOICES, widget=forms.Select(attrs={'class': 'form-control'}))
    zip_code = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'ZIP Code'}))
    account_no = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Account Number'}))
    transaction_id = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Transaction ID'}))
    payment_method = forms.ChoiceField(choices=PAYMENT_METHOD_CHOICES, widget=forms.RadioSelect(attrs={'class': 'form-check-input'}))

    class Meta:
        model = Order
        fields = ['name', 'email', 'phone', 'address', 'division', 'district', 'zip_code', 'payment_method', 'account_no', 'transaction_id']
