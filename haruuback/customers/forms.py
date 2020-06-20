from django import forms
from accounts.models import HaruuUser
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate


class EmailChangeCheckForm(forms.Form):
    """メールアドレス変更フォーム"""

    email = forms.CharField(initial='a',
                            label='現在のメールアドレス',
                            max_length=128,
                            required=False,
                            widget=forms.TextInput(
                                attrs={'v-model': 'special'})
                            )
    after_change_email = forms.CharField(label='変更後メールアドレス',
                                         max_length=128,
                                         required=False)
    confirm_after_change_email = forms.CharField(label='変更後メールアドレス(確認用)',
                                                 max_length=128,
                                                 required=False)
    password = forms.CharField(label='パスワード',
                               max_length=128,
                               required=False)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for k, v in self.fields.items():
            v.widget.attrs['class'] = 'form-control'
            v.widget.attrs["v-model"] = k

    def clean_after_change_email(self):
        after_change_email = self.cleaned_data.get('after_change_email')
        if not after_change_email:
            raise forms.ValidationError('この項目は必須です。')
        HaruuUser.objects.filter(email=after_change_email)
        return after_change_email

    def clean_confirm_after_change_email(self):
        confirm_after_change_email = self.cleaned_data.get(
            'confirm_after_change_email')
        if not confirm_after_change_email:
            raise forms.ValidationError('この項目は必須です。')
        HaruuUser.objects.filter(email=confirm_after_change_email)
        return confirm_after_change_email

    def clean_password(self):
        password = self.cleaned_data.get(
            'password')
        if not password:
            raise forms.ValidationError('この項目は必須です。')
        haruu_user_model = HaruuUser.objects.filter(email=password)
        return password

    def clean_email(self):
        email = self.cleaned_data.get(
            'email')
        if not email:
            raise forms.ValidationError('この項目は必須です。')
        return email

    def clean(self):
        raise Exception("例外が発生しました")
        return after_change_email


class CustomLoginForm(AuthenticationForm):
    """ログインフォーム"""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'
            field.widget.attrs['placeholder'] = field.label
            field.required = False

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if username == '':
            raise forms.ValidationError('この項目は必須です。')
        return username

    def clean_password(self):
        password = self.cleaned_data.get('password')
        if password == '':
            raise forms.ValidationError('この項目は必須です。')
        return password

    def clean(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')

        if username is not None and password:
            self.user_cache = authenticate(self.request, username=username,
                                           password=password)
            if self.user_cache is None:
                raise self.get_invalid_login_error()
            else:
                self.confirm_login_allowed(self.user_cache)

        return self.cleaned_data
