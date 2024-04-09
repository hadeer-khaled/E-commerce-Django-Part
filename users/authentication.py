from django.conf import settings
from rest_framework import authentication, exceptions
import jwt
from . import models
import os
from dotenv import load_dotenv
from pathlib import Path
BASE_DIR = Path(__file__).resolve().parent.parent
dotenv_path = os.path.join(BASE_DIR, 'config', '.env')
load_dotenv(dotenv_path)


class CustomUserAuthentication(authentication.BaseAuthentication):
    def authenticate(self, request):
        token = request.COOKIES.get('jwt')
        print(token)
        try:
            if not token:
                raise exceptions.AuthenticationFailed('No Token Provided:')

            # jwt_secret = os.environ.get('JWT_SECRET')
            payload = jwt.decode(token, os.getenv('JWT_SECRET_KEY'), algorithms=['HS256'])    
        except jwt.ExpiredSignatureError:
            raise exceptions.AuthenticationFailed('Token has expired')   
        # except jwt.InvalidTokenError:
        #     raise exceptions.AuthenticationFailed('Invalid token')   
        except Exception as e:
            raise exceptions.AuthenticationFailed('Failed to authenticate:'+str(e))

        user = models.User.objects.filter(user_id=payload["id"], is_superuser=False).first()

        if user is None:
            raise exceptions.AuthenticationFailed('User does not exist or is a superuser')

        return(user,None)
        