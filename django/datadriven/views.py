from django.views.generic import (ListView)
from . import models


class PortfolioView(ListView):
    """
    Class-based view to show the project list template
    """
    template_name = 'portfolio/project-list.html'
    model = models.Project


class ServicesView(ListView):
    """
    Class-based view to show the services template
    """
    template_name = 'general/services.html'
    model = models.Service
