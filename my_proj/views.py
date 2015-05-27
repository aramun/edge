from django.views import generic


class HomePage(generic.TemplateView):
    template_name = "home.html"


class AboutPage(generic.TemplateView):
    template_name = "about.html"
    
class Contact(generic.TemplateView):
    template_name = "contact.html"
