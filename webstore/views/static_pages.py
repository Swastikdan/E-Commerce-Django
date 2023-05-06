from django.views.generic import TemplateView

class About(TemplateView):
    template_name = "about.html"

class PrivacyPolicy(TemplateView):
    template_name = "privacy_policy.html"

class Licensing(TemplateView):
    template_name = "licensing.html"

class Contact(TemplateView):
    template_name = "contact.html"

class Service(TemplateView):
    template_name = "services.html"