from utils.utils import email_is_valid, phone_is_valid
from apps.platform_health.models import Person
from django.contrib import messages
import re


def login_is_valid(request, username: str, password: str) -> bool:
    if (len(username.strip()) == 0) or len(password.strip()) == 0:
        messages.error(request, 'Preencha todos os campos')
        return False
    return True

def register_is_valid(request, username: str, email: str, phone_number: str, password: str, confirm_password: str, checkbox: bool) -> bool:
    empty_fields = (len(username.strip()) == 0) or (len(email.strip()) == 0) or (len(phone_number.strip()) == 0) or (len(password.strip()) == 0) or (len(confirm_password.strip()) == 0)
    phone_number_exist = Person.objects.filter(phone_number=phone_number).exists()

    if empty_fields:
        messages.error(request, 'Preencha todos os campos')
        return False
    
    if not email_is_valid(request, email):
        return False
        
    if phone_number_exist:
        messages.error(request, 'Número de telefone já cadastrado')
        return False
    
    if not phone_is_valid(request, phone_number):
        return False
    
    if not password_is_valid(request,  password, confirm_password):
        return False
    
    if checkbox is None:
        messages.error(request, 'Você precisa aceitar os termos de serviço')
        return False

    return True

def password_is_valid(request, password: str, confirm_password: str) -> bool:
    password_pattern = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{6,}$'  # Ex4mp!
    password_match = re.match(password_pattern, password)

    if not password_match:
        messages.error(request, 'Senha não é válida')
        return False
    
    if password != confirm_password:
        messages.error(request, 'As senhas não coicidem')
        return False
    
    return True