from django.views.generic import (ListView)
from . import models


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
