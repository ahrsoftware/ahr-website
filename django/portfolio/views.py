from django.views.generic import (ListView)
from . import models


class ProjectListView(ListView):
    """
    Class-based view to show the project list template
    """
    template_name = 'researchdata/project-list.html'
    model = models.Project
