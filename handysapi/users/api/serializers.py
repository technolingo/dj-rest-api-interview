from django.utils.translation import ugettext_lazy as _

from rest_framework import serializers
from django.contrib.auth import authenticate

from ..models import User


class AuthTokenSerializer(serializers.Serializer):
    ''' A serializer that uses email instead of username
        (see settings under section 'ALLAUTH CONFIGURATION')
    '''
    email = serializers.EmailField(label=_("Email Address"))
    password = serializers.CharField(
        label=_("Password"),
        style={'input_type': 'password'},
        trim_whitespace=False
    )

    def validate(self, data):
        email = data.get('email')
        password = data.get('password')

        if email and password:
            user = authenticate(email=email, password=password)

            if user is not None:
                if not user.is_active:
                    msg = _('User account is deactivated.')
                    raise serializers.ValidationError(msg)
            else:
                msg = _('Unable to log in with provided credentials.')
                raise serializers.ValidationError(msg)
        else:
            msg = _('Must include "email" and "password".')
            raise serializers.ValidationError(msg)

        data['user'] = user
        return data


class UserModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'email', 'password', 'name', 'birthday',
        ]
