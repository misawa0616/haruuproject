from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from .forms import EmailChangeCheckForm
from django.shortcuts import render
from accounts.models import HaruuUser
from django.contrib.auth.views import LoginView, LogoutView
from .forms import CustomLoginForm


class EmailChangeCheckView(generic.FormView):
    """メールアドレスの変更"""
    template_name = 'customers/email_change.html'
    form_class = EmailChangeCheckForm

    def get_initial(self):
        initial = {'before_change_email': self.request.user.email}
        return initial.copy()

    def form_valid(self, form):
        return render(self.request, 'customers/email_change.html', {
            'form': form,
        })

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        form.data.email = self.request.user.email
        form_valid = form.is_valid()
        if form_valid == 1:
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs


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
