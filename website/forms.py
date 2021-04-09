from django import forms

class Usr_answers(forms.Form):
    usr_answer = forms.CharField(widget=forms.TextInput())