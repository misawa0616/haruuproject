from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from .forms import EmailChangeCheckForm, CustomLoginForm, EmailChangeForm
from django.shortcuts import render
from accounts.models import HaruuUser
from django.urls import reverse_lazy, reverse
from django.contrib.auth.views import LoginView, LogoutView
from django.http import HttpResponseRedirect, HttpResponseBadRequest
from django.contrib.auth import get_user_model


class EmailChangeCheckView(generic.FormView):
    """メールアドレスの変更チェック"""
    template_name = 'customers/email_change.html'
    success_url = reverse_lazy('customers:email_change_confirm')
    form_class = EmailChangeCheckForm

    def get_initial(self):
        initial = {'before_change_email': self.request.user.email}
        return initial.copy()

    def form_valid(self, form):
        self.request.session['after_change_email'] = form.cleaned_data.get(
            'after_change_email')
        return super().form_valid(form)

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs


class EmailChangeView(generic.FormView):
    """メールアドレスの変更"""
    template_name = 'customers/email_change_confirm.html'
    form_class = EmailChangeForm

    def get(self, request, *args, **kwargs):
        if not self.request.session.get('after_change_email'):
            return HttpResponseRedirect(reverse('customers:email_change'))
        return super().get(request, *args, **kwargs)

    def get_initial(self):
        if self.request.session.get('after_change_email'):
            self.initial = {'after_change_email': self.request.session.get(
                'after_change_email')}
        return self.initial.copy()

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.initial.get('after_change_email') == self.request.session.get('after_change_email'):
            user_model = get_user_model().objects.get(email=self.request.user.email)
            user_model.email = self.request.session.get('after_change_email')
            user_model.save()
            del request.session['after_change_email']
            return HttpResponseRedirect(reverse('customers:email_change_complete'))
        else:
            return HttpResponseBadRequest


class CustomLoginView(LoginView):
    form_class = CustomLoginForm
    template_name = 'customers/login.html'

    def post(self, request, *args, **kwargs):
        """
        Handle POST requests: instantiate a form instance with the passed
        POST variables and then check if it's valid.
        """
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)


class CustomLogoutView(LogoutView):
    """ログアウトページ"""
    template_name = 'customers/top.html'


class TopView(LoginRequiredMixin, generic.TemplateView):
    template_name = 'customers/top.html'

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        return self.render_to_response(context)

    def get_initial(self):
        initial = {'email': self.request.user.email}
        return initial.copy()
