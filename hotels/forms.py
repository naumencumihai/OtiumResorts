from django import forms

class DateForm(forms.Form):
     start_date = forms.DateField(input_formats = ['%m/%d/%Y'])
     end_date = forms.DateField(input_formats = ['%m/%d/%Y'])