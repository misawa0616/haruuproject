from .models import EmailConfirm, HaruuUser
from rest_auth.serializers import LoginSerializer
from rest_framework import serializers


class ChangeEmailSerializer(serializers.ModelSerializer):

    class Meta:
        model = EmailConfirm
        exclude = ['created_at', 'is_complete']

    def validate_email(self, attrs):
        if HaruuUser.objects.filter(email=attrs).exists():
            raise serializers.ValidationError("このメールアドレスは既に登録されています。")

        return attrs


class HaruuUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = HaruuUser
        exclude = ['password', 'username']

class CustomLoginSerializer(LoginSerializer):

    email = serializers.EmailField(required=True, allow_blank=False)
