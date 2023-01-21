from django import forms
from django.core.mail import send_mail
import logging
logger = logging.getLogger(__name__)
class ContactForm(forms.Form):
    name=forms.CharField(max_length=100)
    email=forms.EmailField()
    content=forms.CharField(widget=forms.Textarea)
 
    