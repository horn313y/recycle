from django import forms
#from captcha.fields import CaptchaField

class CsvImportForm(forms.Form):
    csv_file = forms.FileField()
    