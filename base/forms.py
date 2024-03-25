from django import forms

from django_recaptcha.fields import ReCaptchaField
from django_recaptcha.widgets import ReCaptchaV3


class ContactForm(forms.Form):
    name = forms.CharField(label='Your Name', max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(label='Your Email', max_length=100, widget=forms.EmailInput(attrs={'class': 'form-control'}))
    subject = forms.CharField(label='Subject', max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    message = forms.CharField(label='Message', widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 4}))
    captcha = ReCaptchaField(widget=ReCaptchaV3)