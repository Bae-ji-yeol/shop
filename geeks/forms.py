from django import forms
from .models import GeeksModel


# creating a form
class GeeksForm(forms.ModelForm):

    class Meta:
        model = GeeksModel
        fields = ['geeks_field']




