#from django.contrib.auth import backends
from member.models import User
from django.contrib.auth.models import User as DjangoUser
#import time
from datetime import datetime
from django.contrib.auth.hashers import make_password, check_password
from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import authenticate, login

class MyModelBackend(ModelBackend):

    def authenticate(self, username=None, password=None):

        if username is not  None:
            try:
                user = User.objects.get(username=username)
                # Check password part from Symfony2
                password1 = make_password(password, user.salt)
                if check_password(password, user.password):
                    user.last_login = datetime.now()
                    return user
                else:
                    print 'User not Authenticated'
            except User.DoesNotExist:
                print "### No User ###"
                return None    

    def get_user(self, user_id):
        try:
            user = User.objects.get(pk=user_id)
            if user.enabled and not user.expired:
                return user
            return None
        except User.DoesNotExist:
            return None


