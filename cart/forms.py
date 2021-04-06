from django import forms


class CheckForm(forms.Form):
    check = forms.BooleanField()


