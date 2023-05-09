from django.views.generic import TemplateView

class About(TemplateView):
    template_name = "about.html"

class PrivacyPolicy(TemplateView):
    template_name = "privacy_policy.html"

class faq(TemplateView):
    template_name = "faq.html"

class Service(TemplateView):
    template_name = "services.html"