from abc import ABC

from django.http import Http404
from django.utils.translation import ugettext_lazy as _
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import HaruuUser
from .models import EmailConfirm
from django.shortcuts import get_object_or_404
from .serializers import ChangeEmailSerializer, HaruuUserSerializer
import uuid
from accounts.models import CustomToken
from rest_framework.permissions import IsAuthenticated
from accounts.authentication import CustomTokenAuthentication
from django.utils import timezone
import datetime
from rest_framework.permissions import AllowAny
from django.core.mail import send_mail


class ConfirmEmailAPIView(APIView):

    permission_classes = (AllowAny,)
    allowed_methods = ('GET', 'HEAD')

    def get(self, request, *args, **kwargs):
        try:
            email_confirmation = get_object_or_404(
                EmailConfirm, token=kwargs['key'])
            haruu_user = get_object_or_404(
                HaruuUser, id=email_confirmation.haruu_user.id)
        except Http404:
            return Response({'detail': _('Invalid input.')},
                            status=status.HTTP_404_NOT_FOUND)

        if email_confirmation.is_complete:
            return Response({'detail': _('Already completed.')},
                            status=status.HTTP_400_BAD_REQUEST)

        if (timezone.now() - email_confirmation.created_at) \
                > datetime.timedelta(days=1):
            return Response({'detail': _('Expired email token.')},
                            status=status.HTTP_400_BAD_REQUEST)

        haruu_user_serializer = HaruuUserSerializer(
            instance=haruu_user, data={'email': email_confirmation.email})
        haruu_user_serializer.is_valid(raise_exception=True)
        haruu_user_serializer.save()
        email_confirmation.is_complete = True
        email_confirmation.save()
        return Response({'detail': _('Successfully confirmed email.')},
                        status=status.HTTP_200_OK)


class ChangeEmailAPIView(APIView):

    authentication_classes = (CustomTokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    allowed_methods = ('POST', 'HEAD')

    def post(self, request, *args, **kwargs):
        get_object_or_404(CustomToken, user=request.data['haruu_user'])
        request_data = request.data
        request_data['token'] = uuid.uuid4().hex
        serializer = ChangeEmailSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        send_mail(
            'mail address confirm',
            'http://127.0.0.1:8000/rest-auth/accounts/'
            'account-confirm-email/{}'.format(serializer.data['token']),
            'takumajane1@outlook.jp',
            [serializer.data['email']],
            fail_silently=False,
        )
        return Response(serializer.data, status.HTTP_201_CREATED)
