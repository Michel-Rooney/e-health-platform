from utils.utils import email_is_valid, phone_is_valid
from django.contrib import messages


def contact_is_valid(request, name: str, email: str, phone: str, message: str):
    empty_fields = (len(name.strip()) == 0) or (len(email.strip()) == 0) or (len(phone.strip()) == 0) or (len(message.strip()) == 0)

    if empty_fields:
        messages.error(request, 'Preencha todos os campos')
        return False
    
    if not email_is_valid(request, email):
        return False
    
    if not phone_is_valid(request,  phone):
        return False
    
    return True