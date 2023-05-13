from django.db import models
from django.core.mail import send_mail
from django.db.models.signals import post_save
from django.dispatch import receiver

class Contact(models.Model):
    email = models.EmailField()
    subject = models.CharField(max_length=255)
    message = models.TextField()

    def __str__(self):
        return self.email
@receiver(post_save, sender=Contact)
def send_new_contact_notification_email(sender, instance, created, **kwargs):
    if created:
        email = instance.email
        subject = instance.subject
        message = instance.message

    send_mail(
        f"New contact message: {subject}",
        f"Sender Mail :\n\n{email}\n\nMessage:\n\n{message}", # Combine email and message in the email body
        'your_email@example.com', # Replace the "from" email with your own email address
        ['your_email@example.com'], # Replace the recipient list with your own email address
        fail_silently=False,
)


