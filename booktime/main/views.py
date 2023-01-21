from os import path
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.edit import FormView
from main import forms 
from .forms import  ContactForm
from main import views
# Create your views here.
def home(request):
    return render(request, "home.html", {})
def about_us(request):
    return render(request, "about_us.html", {})

def contact_us(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)

        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            content = form.cleaned_data['content']

            html = render_to_string('contact_form.html', {
                'name': name,
                'email': email,
                'content': content
            })

            send_mail('The contact form subject', 'This is the message', 'noreply@codewithstein.com', ['codewithtestein@gmail.com'], html_message=html)

            return redirect('contact_us')
    else:
        form = ContactForm()

    return render(request, 'contact_form.html', {
        'form': form
    })