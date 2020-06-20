import uuid
from django.db import models
from django.contrib.auth.models import AbstractUser
from rest_framework.authtoken.models import Token


class Application(models.Model):

    id = models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    email = models.EmailField(max_length=254, unique=True)
    token = models.CharField(default=uuid.uuid4().hex, max_length=32)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 't2_application'
        db_table = 't2_application'
        verbose_name = 'id'


class HaruuUser(AbstractUser):
    email = models.EmailField(blank=True)
    application = models.ForeignKey(Application, blank=True, null=True, on_delete=models.CASCADE)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta(AbstractUser.Meta):
        swappable = 'AUTH_USER_MODEL'
        verbose_name_plural = 't1_haruu_user'
        db_table = 't1_haruu_user'


class EmailConfirm(models.Model):
    id = models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    haruu_user = models.ForeignKey(HaruuUser, blank=True, null=True, on_delete=models.CASCADE)
    email = models.EmailField(max_length=254)
    token = models.CharField(default=uuid.uuid4().hex, max_length=32)
    created_at = models.DateTimeField(auto_now_add=True)
    is_complete = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = 't3_email_confirm'
        db_table = 't3_email_confirm'
        verbose_name = 'id'


class CustomToken(Token):
    id = models.AutoField(
        auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    key = models.CharField(default=uuid.uuid4().hex, max_length=32)
    updated_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 't4_custom_token'
        db_table = 't4_custom_token'
