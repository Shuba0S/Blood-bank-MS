from django.shortcuts import render
from django.conf import settings
from django.core.mail import send_mail
from django.http import HttpResponse
import logging

logger = logging.getLogger(__name__)

def contact_us(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        try:
            send_mail(
                subject=f"Message from {name} - {subject}",
                message=message,
                from_email=email,
                recipient_list=settings.EMAIL_RECEIVING_USER,
                fail_silently=False,
            )
            return render(request, 'blood/contact_us.html', {'message': 'Your message has been sent successfully!'})
        except Exception as e:
            logger.error(f"Error sending email: {e}")
            return render(request, 'blood/contact_us.html', {'message': 'There was an error sending your message.'})

    return render(request, 'blood/contact_us.html')
