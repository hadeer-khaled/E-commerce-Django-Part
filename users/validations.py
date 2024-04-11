from django.core.exceptions import ValidationError
from django.contrib.auth import get_user_model
User = get_user_model()

def custom_validation(data):
    email = data['email'].strip()
    password = data['password'].strip()
    phone = data['phone'].strip()
    first_name = data['first_name'].strip()
    last_name = data['last_name'].strip()
    
    if not email or User.objects.filter(email=email).exists():
        raise ValidationError('Email already exists')
    
    if not phone or User.objects.filter(phone=phone).exists():
        raise ValidationError('Phone number already exists')
    
    if not password or len(password) < 8:
        raise ValidationError('choose another password, min 8 characters')
    
    if not first_name:
            raise ValidationError('First name is required')
        
    if not last_name:
            raise ValidationError('Last name is required')
    return data


def validate_email(data):
    email = data['email'].strip()
    if not email or len(email) != 2:
        raise ValidationError('an email is needed')
    return True

def validate_password(data):
    password = data['password'].strip()
    if not password:
        raise ValidationError('a password is needed')
    return True

def validate_phone(data):
    phone = data['phone'].strip()
    if not phone:
        raise ValidationError('Phone is required')

    if phone[0:4] not in ['011','012','015','010'] or len(phone) != 11 :
        raise ValidationError('The number is not Egyptian number')
    return True