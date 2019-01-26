from django import forms
from .models import (
    Activity,
    Countries,
    Destination,
    CitizenshipCountries
)


class PlanForm(forms.Form):
    countries = forms.ChoiceField(choices=tuple([(u'', "Select your country")] + list(Countries.objects.all().values_list('id', 'country'))), widget=forms.Select(attrs={'class': 'btn btn-secondary dropdown-toggle', 'style': "background-color: #00CCCD; width: 250px"}))
    activities = forms.ChoiceField(choices=tuple([(u'', "Select your path")] + list(Activity.objects.all().values_list('id', 'activity'))), widget=forms.Select(attrs={'class': 'btn btn-secondary dropdown-toggle', 'style': "background-color: #00CCCD; width: 250px"}))
    destinations = forms.ChoiceField(choices=tuple([(u'', "Select your destination")] + list(Destination.objects.all().values_list('id', 'destination'))), widget=forms.Select(attrs={'class': 'btn btn-secondary dropdown-toggle', 'style': "background-color: #00CCCD; width: 250px"}))


class CitizenshipForm(forms.Form):
    citizenship_countries = forms.ChoiceField(choices=tuple([(u'', "Select a country")] + list(CitizenshipCountries.objects.all().values_list('id', 'citizenship_country'))), widget=forms.Select(attrs={'class': 'btn btn-secondary dropdown-toggle', 'style': "background-color: #00CCCD; width: 350px", 'onchange': "this.form.submit()"}))


class ContactForm(forms.Form):
    from_email = forms.EmailField(label='', widget=forms.TextInput(attrs={'type': 'email', 'placeholder': "Please enter your email *", 'class': "form-control"}), required=True)
    subject = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': 'Please enter a subject *', 'class': "form-control"}), max_length=50, required=True)
    message = forms.CharField(label='', widget=forms.Textarea(attrs={'class': "form-control", 'placeholder': "Please enter your message here *"}), required=True)
