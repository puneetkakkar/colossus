from django import forms


class form_signup(forms.Form):
    full_name = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Full Name'}), label='')
    username_email = forms.EmailField(widget=forms.TextInput(attrs={
        'placeholder': 'Email'}), label='')
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Password'}), label='')
    # widgets = {'password': forms.PasswordInput(),}


class form_login(forms.Form):
    email = forms.EmailField(widget=forms.TextInput(attrs={
        'placeholder': 'Email'}), label='')
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Password'}), label='')
