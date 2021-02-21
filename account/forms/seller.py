from django import forms
from account.models.seller import Seller

class SellerForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    confirm_password = forms.CharField(widget=forms.PasswordInput())
    email = forms.EmailField()
    class Meta:
        model = Seller
        fields = [
            'first_name', 'last_name', 'phone', 'email', 'password'
        ]
    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')

        if password != confirm_password:
            raise forms.ValidationError(
                "Password does not match"
        )

class SellerLoginForm(forms.Form):
    email    = forms.EmailField(label='Email')
    password = forms.CharField(widget=forms.PasswordInput)