from django import forms
from .models import PhoneNumberCSV


class PNCSVModelForm(forms.ModelForm):
    class Meta:
        model = PhoneNumberCSV
        fields = ('file_name',)
