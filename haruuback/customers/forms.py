from django import forms
from accounts.models import HaruuUser
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate
from django.contrib.auth import get_user_model

HARUUCODE0000 = "エラーがあります。"
HARUUCODE0001 = "この項目は必須です。"
HARUUCODE0002 = "{}以内で入力してください。"
HARUUCODE0003 = "確認メールアドレスが一致しません。"
HARUUCODE0004 = "このメールアドレスは既に登録されています。"
HARUUCODE0005 = "パスワードが違います。"


class EmailChangeCheckForm(forms.Form):
    """メールアドレス変更フォーム"""

    before_change_email = forms.CharField(label='現在のメールアドレス',
                                          max_length=128,
                                          required=False,
                                          )
    after_change_email = forms.CharField(label='変更後のメールアドレス',
                                         max_length=128,
                                         required=False,
                                         widget=forms.TextInput(
                                             attrs={
                                                 'placeholder': 'abcde@co.jp',
                                                 'v-model': 'after_change_email',
                                                 'v-bind:class': '{ error: after_change_email_error }'})
                                         )
    after_change_email_confirm = forms.CharField(label='変更後のメールアドレス(確認用)',
                                                 max_length=128,
                                                 required=False,
                                                 widget=forms.TextInput(
                                                     attrs={
                                                         'placeholder': 'abcde@co.jp',
                                                         'v-model': 'after_change_email_confirm',
                                                         'v-bind:class': '{ error: after_change_email_confirm_error }'})
                                                 )
    password = forms.CharField(label='パスワード',
                               max_length=128,
                               required=False,
                               widget=forms.PasswordInput(
                                   attrs={
                                       'v-model': 'password',
                                       'v-bind:class': '{ error: password_error }'})
                               )

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        super().__init__(*args, **kwargs)

    def validate_required(self, after_change_email, after_change_email_confirm,
                          password):
        if not after_change_email:
            self.add_error('after_change_email', HARUUCODE0001)
        if not after_change_email_confirm:
            self.add_error('after_change_email_confirm', HARUUCODE0001)
        if not str.strip(password):
            self.add_error('password', HARUUCODE0001)
        if self.errors:
            raise forms.ValidationError(HARUUCODE0000)

    def validate_format(self, after_change_email, after_change_email_confirm):
        if len(after_change_email) > 60:
            self.add_error('after_change_email', HARUUCODE0002.format(60))
        if len(after_change_email_confirm) > 60:
            self.add_error('after_change_email_confirm',
                           HARUUCODE0002.format(60))
        if self.errors:
            raise forms.ValidationError(HARUUCODE0000)

    def validate_match(self, after_change_email, after_change_email_confirm):
        if after_change_email != after_change_email_confirm:
            self.add_error('after_change_email_confirm',
                           HARUUCODE0003)
        if self.errors:
            raise forms.ValidationError(HARUUCODE0000)

    def validate_duplicate(self, after_change_email):
        email_filter = get_user_model().objects.filter(email=after_change_email)
        if email_filter.count() >= 1:
            self.add_error('after_change_email',
                           HARUUCODE0004)
        if self.errors:
            raise forms.ValidationError(HARUUCODE0000)

    def validate_authenticate(self, password):
        if not self.user.check_password(password):
            self.add_error('password', HARUUCODE0005)
        if self.errors:
            raise forms.ValidationError(HARUUCODE0000)

    def clean(self):
        after_change_email = self.cleaned_data.get('after_change_email')
        after_change_email_confirm = self.cleaned_data.get(
            'after_change_email_confirm')
        password = self.cleaned_data.get('password')
        self.validate_required(after_change_email, after_change_email_confirm,
                               password)
        self.validate_format(after_change_email, after_change_email_confirm)
        self.validate_match(after_change_email, after_change_email_confirm)
        self.validate_duplicate(after_change_email)
        self.validate_authenticate(password)
        return self.cleaned_data


class EmailChangeForm(forms.Form):
    """メールアドレス変更フォーム"""

    after_change_email = forms.CharField(label='変更後のメールアドレス',
                                         max_length=128,
                                         required=False,
                                         )


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
