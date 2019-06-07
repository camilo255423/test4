from django import forms
from django.core.validators import validate_slug, validate_email


class PersonForm(forms.Form):
    nombre = forms.CharField(max_length=200, validators=[validate_slug, validate_email])
