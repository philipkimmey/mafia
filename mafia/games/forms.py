from django import forms

class GameForm(forms.Form):
    num_participants = forms.CharField(label=u'num_participants', max_length=30)
    emails = forms.CharField(label=u'emails', widget=forms.PasswordInput())