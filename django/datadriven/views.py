from django.views.generic import (CreateView, ListView, TemplateView)
from . import models, forms
from django.urls import reverse_lazy


class ContactCreateView(CreateView):
    """
    Class-based view to show the  template
    """
    template_name = 'datadriven/contact.html'
    form_class = forms.ContactForm
    success_url = reverse_lazy('contact')


class ContactCreateSuccessTemplateView(TemplateView):
    """
    Class-based view to show the message create success template
    """
    template_name = 'datadriven/contact-success.html'


class PortfolioView(ListView):
    """
    Class-based view to show the project list template
    """
    template_name = 'datadriven/portfolio.html'
    model = models.Project


class ServicesView(ListView):
    """
    Class-based view to show the services template
    """
    template_name = 'datadriven/services.html'
    model = models.Service
