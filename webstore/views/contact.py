# This is a Django view class for handling GET and POST requests for a contact form, which saves the
# submitted data to the database and displays a success message.
from django.shortcuts import render, redirect
from django.contrib import messages
from django.views import View
from webstore.models.contact import Contact

class ContactView(View):
    def get(self, request):
        return render(request, 'contact.html')

    def post(self, request):
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        messages.success(request, 'Your message has been sent successfully!')
        return redirect('contact')
''' This Part is for Gmail Intregation  '''

        # contact = Contact(email=email, subject=subject, message=message)
        # contact.save()


