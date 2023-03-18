from django import forms


class ContactForm(forms.Form):
    title = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'insert'}))
    message = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'insert'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder': 'insert'}))
