from django import forms
from .models import kontak

class data(forms.Form):
    email = forms.EmailField(required=False)
    nama = forms.CharField(required=False)
    no_hp = forms.IntegerField(max_value=12)
    no_rek = forms.IntegerField()
    setuju = forms.BooleanField(required=False)


class postKontak(forms.ModelForm):
    class Meta:
        model = kontak
        fields = ['nama', 'hp', 'email']