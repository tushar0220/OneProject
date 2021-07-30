from django.contrib.auth.signals import user_logged_in, user_logged_out, user_login_failed
from django.contrib.auth.models import User
from django.dispatch import receiver

@receiver(user_logged_in, sender=User)
def loginRcv(sender, request, user, **kwargs):
    print('------------------------------------------------------')
    print('Logged in signal - Run Intro')
    print('sender : ', sender)
    print('request : ', request)
    print('user : ', user)
    print('user password : ', user.password)
    print(f'kwargs: {kwargs}')
#user_logged_in.connect(loginRcv, sender=User)

def logoutRcv(sender, request, user, **kwargs):
    print('------------------------------------------------------')
    print('Logged out signal - Run Outro')
    print('sender : ', sender)
    print('request : ', request)
    print('user : ', user)
    print('user password : ', user.password)
    print(f'kwargs: {kwargs}')
user_logged_out.connect(logoutRcv, sender=User)

@receiver(user_login_failed)
def login_failed(sender, request, credentials, **kwargs):
    print('------------------------------------------------------')
    print('Login Failed signal - Run Outro')
    print('sender : ', sender)
    print('request : ', request)
    print('Credentials : ', credentials)
    print(f'kwargs: {kwargs}')

