from django.db import models

#token modules

class Laptop(models.Model):
    CHARGER = 'CR'
    MOUSE = 'MU'

    FREE = [
        (CHARGER, 'Charger'),
        (MOUSE, 'Mouse'),
    ]

    des = ["Charger","Mouse"]
    name = models.CharField(max_length=100)
    free = models.CharField(max_length=2, choices= FREE, default= 'Charger')
    cost = models.IntegerField()
    #description = models.Field(max_length=200)

    def __str__(self):
        return self.name

class Registration(models.Model):
    username = models.CharField(max_length=100)
    email = models.EmailField(max_length=50, unique= True)
    password = models.CharField(max_length=100)
    date_joined = models.DateTimeField(verbose_name='date joined',auto_now_add=True)
    last_login = models.DateTimeField(verbose_name= 'last login',auto_now=True)
    is_admin = models.BooleanField(default= False)
    is_active = models.BooleanField(default= True)
    is_staff = models.BooleanField(default= False)

    def __str__(self):
        return self.email

# @receiver(post_save, sender = settings.AUTH_USER_MODEL)
# def create_auth_token(sender, instance = None, created = False, **kwargs):
#     if created:
#         Token.objects.create(uesee = )
