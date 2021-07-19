from rest_framework import serializers

from .models import Laptop, Registration


class LaptopSerializer(serializers.ModelSerializer):
    class Meta:
        model = Laptop
        fields = '__all__'

class RegistrationSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style={'input_type':'password'}, write_only= True)

    class Meta:
        model = Registration
        fields = ['id','username','email','password','password2']
        extra_kwargs = {
                'password': {'write_only': True}
        }

    def validate(self,attrs):
        if Registration.objects.filter(email = attrs['email']).exists():
            raise serializers.ValidationError({'email':'email already exists, try with other'})
        elif Registration.objects.filter(username = attrs['username']).exists():
            raise serializers.ValidationError({'user': 'user already exists, try with other'})
        return super().validate(attrs)
    def save(self):
        register = Registration(email = self.validated_data['email'],
                        username = self.validated_data['username'],
                        )
        register.is_admin = True
        register.is_staff = True

        password = self.validated_data['password']
        password2 = self.validated_data['password2']

        if password != password2:
            raise serializers.ValidationError({'password':'Password must match.'})
        # register.set_password(password)
        register.save()
        return register
