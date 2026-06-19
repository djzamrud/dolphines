from django import forms
from .models import kontak

class postKontak(forms.ModelForm):
    class Meta:
        model = kontak
        fields = ['nama', 'no_hp', 'email', 'pesan']