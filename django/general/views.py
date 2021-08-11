from django.views.generic import TemplateView


class WelcomeTemplateView(TemplateView):
    """
    Welcome-based view to show the welcome template
    """
    template_name = 'general/welcome.html'


class ServicesTemplateView(TemplateView):
    """
    Class-based view to show the services template
    """
    template_name = 'general/services.html'


class CookiesTemplateView(TemplateView):
    """
    Class-based view to show the cookies template
    """
    template_name = 'general/cookies.html'
