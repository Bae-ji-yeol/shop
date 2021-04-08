from django import forms
from .models import CartItem


class CheckForm(forms.ModelForm):

    class Meta:
        model = CartItem
        fields = ['check']
