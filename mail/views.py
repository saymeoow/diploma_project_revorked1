from .forms import ContactForm
from django.views.generic import FormView, TemplateView


class SendMailView(FormView):
    template_name = 'email.html'
    success_url = '/mail/success/'
    form_class = ContactForm


class SuccessView(TemplateView):
    template_name = 'success.html'
