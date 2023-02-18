from django.contrib import messages
import re

def login_is_valid(request, username: str, password: str) -> bool:
    if (len(username.strip()) == 0) or len(password.strip()) == 0:
        messages.error(request, 'Preencha todos os campos')
        return False
    return True

