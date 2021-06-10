from django import forms


class UserForm(forms.Form):
    firstname = forms.CharField(max_length=15)
    lastname = forms.CharField(max_length=15)
    age = forms.IntegerField(min_value=1, max_value=99)
