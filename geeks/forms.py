from django import forms


# creating a form
class GeeksForm(forms.Form):
    geeks_field = forms.BooleanField(required=False)


