from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.conf import settings
from django.contrib.auth.models import User
from django.contrib import messages
import re


def email_is_valid(request, email: str) -> bool:
    email_exist = User.objects.filter(email=email).exists()
    email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'  # example@email.com
    email_match = re.match(email_pattern, email)

    if email_exist:
        messages.error(request, 'Email já cadastrado')
        return False

    if not email_match:
        messages.error(request, 'Email não é valido')
        return False
    
    return True

def phone_is_valid(request, phone_number: str) -> bool:
    phone_number_pattern = r'^\+55\s*\(?(\d{2})\)?[-.\s]*(\d{5})[-.\s]*(\d{4})$'  # +55 (XX) XXXXX-XXXX
    phone_number_match = re.match(phone_number_pattern, phone_number)
    
    if not phone_number_match:
        messages.error(request, 'O número de telefone não é válido')
        return False
    
    return True

def send_email(path_template: str, subject: str, to: list, **kwargs) -> dict:
    html_content = render_to_string(path_template, kwargs)
    text_content = strip_tags(html_content)

    email = EmailMultiAlternatives(subject, text_content, settings.EMAIL_HOST_USER, to)

    email.attach_alternative(html_content, "text/html")
    email.send()
    return {'status': 1}
