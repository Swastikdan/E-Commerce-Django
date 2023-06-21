
"""
    This is a Python code defining views for different web pages and custom error pages for a Django web
    application.
    
    :param request: The HTTP request object that contains information about the current request, such as
    the user agent, requested URL, and any submitted data
    :param exception: The exception parameter is used in the custom_404 function to handle any
    exceptions that occur when a user tries to access a page that does not exist. It is a built-in
    Django parameter that captures the exception that caused the 404 error
    :return: The code defines several views using the TemplateView class from Django. Each view
    specifies a template to render when the view is accessed. Additionally, there are two error handling
    views defined: custom_404 and custom_500. These views return a rendered template for the
    corresponding HTTP error status codes.
"""
from django.views.generic import TemplateView
class About(TemplateView):
    template_name = "about.html"

class PrivacyPolicy(TemplateView):
    template_name = "privacy_policy.html"

class faq(TemplateView):
    template_name = "faq.html"

class Service(TemplateView):
    template_name = "services.html"
def custom_404(request, exception):
    return render(request, '404.html', status=404)

def custom_500(request):
    return render(request, '500.html', status=500)
