from django.urls import path
from .  import views
from django.views.generic import TemplateView
from main import views
app_name='main'
urlpatterns = [
    path("contact-us/",TemplateView.as_view(template_name="pages/contact_form.html"),name="home",),
     path("about-us/",TemplateView.as_view(template_name="pages/about_us.html"),name="about_us",),
     path("",TemplateView.as_view(template_name="pages/home.html"),name="home",),
]

