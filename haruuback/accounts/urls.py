from django.conf.urls import url
from .views import ConfirmEmailAPIView, ChangeEmailAPIView

urlpatterns = [
    url(r'^account-confirm-email/(?P<key>[-:\w]+)/$',
        ConfirmEmailAPIView.as_view(),
        name='account_confirm_email'),
    url(r'^change-email/',
        ChangeEmailAPIView.as_view(),
        name='change_email'),
]
