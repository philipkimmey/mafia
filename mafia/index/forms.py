from django import forms

class RegistrationForm(forms.Form):
    username = forms.CharField(label=u'Username', max_length=30)
    password = forms.CharField(label=u'Password', widget=forms.PasswordInput())