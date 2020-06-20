import uuid
from django.utils import timezone


def custom_create_token(token_model, user, serializer):
    token, _ = token_model.objects.update_or_create(
        user=user, defaults={'key': uuid.uuid4().hex,
                             'updated_at': timezone.now()})
    return token
