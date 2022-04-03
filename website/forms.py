from django import forms
from website.models import Contact, Newsletter


class CantactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'

class NewsletterForm(forms.ModelForm):
    class Meta:
        model = Newsletter
        fields = '__all__'
