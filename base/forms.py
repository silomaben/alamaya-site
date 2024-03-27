from django import forms
from django.forms.widgets import DateTimeInput

from django_recaptcha.fields import ReCaptchaField
from django_recaptcha.widgets import ReCaptchaV3


class ContactForm(forms.Form):
    name = forms.CharField(label='Your Name', max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(label='Your Email', max_length=100, widget=forms.EmailInput(attrs={'class': 'form-control'}))
    subject = forms.CharField(label='Subject', max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    message = forms.CharField(label='Message', widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 4}))
    captcha = ReCaptchaField(widget=ReCaptchaV3)


class BookingForm(forms.Form):
    name = forms.CharField(label='Your Name', max_length=100, widget=forms.TextInput(attrs={'class': 'form-control bg-transparent', 'style': 'color: white;'}))
    email = forms.EmailField(label='Your Email', max_length=100, widget=forms.EmailInput(attrs={'class': 'form-control bg-transparent', 'style': 'color: white;'}))
    phone_no = forms.CharField(label='Your Phone Number', max_length=15, widget=forms.TextInput(attrs={'class': 'form-control bg-transparent', 'style': 'color: white;'}))
    number_of_guests = forms.IntegerField(
        label='Number of Guests',
        widget=forms.NumberInput(attrs={'class': 'form-control bg-transparent', 'style': 'color: white;'}),
        min_value=1,
        max_value=14,
        initial=1,
        help_text='Enter a number between 0 and 14'
    )
    datetime_from = forms.DateTimeField(input_formats=['%m/%d/%Y %I:%M %p'],
                widget=DateTimeInput(
                    attrs={
                        'class': 'form-control bg-transparent datetimepicker-input',
                        'style': 'color: white;',
                        'placeholder': 'Date From:',
                        'data-target': '#dateFrom',
                        'data-toggle': 'datetimepicker',
                        'name': 'datetime',
                        'id': 'datetime'
                    },format='%m/%d/%Y %I:%M %p'
                )
            )
    datetime_to = forms.DateTimeField(input_formats=['%m/%d/%Y %I:%M %p'],
                widget=DateTimeInput(
                    attrs={
                        'class': 'form-control bg-transparent datetimepicker-input',
                        'style': 'color: white;',
                        'placeholder': 'Date To:',
                        'data-target': '#dateTo',
                        'data-toggle': 'datetimepicker',
                        'name': 'datetime',
                        'id': 'datetime'
                    },format='%m/%d/%Y %I:%M %p'
                )
            )

    # number_of_guests = forms.IntegerField(label='Number of Guests', min_value=0, max_value=14, initial=1, widget=forms.NumberInput(attrs={'class': 'form-control bg-transparent', 'style': 'color: white;'}))
    destination = forms.ChoiceField(label='Destination', choices=[('', 'Select a destination'), ('Maasai Mara', 'Maasai Mara'), ('Tsavo', 'Tsavo'), ('Olpejeta', 'Olpejeta'), ('Samburu', 'Samburu'), ('Amboseli', 'Amboseli'), ('Diani', 'Diani'), ('Lake Naivasha', 'Lake Naivasha'), ('Kakamega Forest', 'Kakamega Forest'), ('Nkare Ntare', 'Nkare Ntare'), ('Mt. Kenya', 'Mt. Kenya'), ('Chalbi Desert', 'Chalbi Desert')], widget=forms.Select(attrs={'class': 'form-select custom-select', 'style': 'color: white;'}))
    special_request = forms.CharField(label='Special Request', required=False,widget=forms.Textarea(attrs={'class': 'form-control bg-transparent', 'style': 'color: white; height: 100px;'}))
    captcha = ReCaptchaField(widget=ReCaptchaV3)
