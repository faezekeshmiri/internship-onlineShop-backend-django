from rest_framework import serializers
from .models import Account


class RegistrationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Account
        fields = ['phone', 'first_name', 'last_name', 'password']

        def save(self):
            account = Account(
                phone=self.validated_data['phone'],
                first_name=self.validated_data['first_name'],
                last_name=self.validated_data['last_name'],
            )
            password = self.validated_data['password']
            account.set_password(password)
            account.save()
            return account
