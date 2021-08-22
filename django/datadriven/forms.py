from django import forms
from . import models
from captcha.fields import ReCaptchaField, ReCaptchaV3
from django.utils.translation import ugettext_lazy as _


class ContactForm(forms.ModelForm):
    """
    A form for users to submit a Message via the Contact page
    """

    customer_name = forms.CharField(label=_('Name'),
                                    required=True)
    customer_email = forms.EmailField(label=_('Email'),
                                      required=True)
    message_text = forms.CharField(widget=forms.Textarea(attrs={'rows': 6}),
                                   label=_('Message'),
                                   required=True)

    # Google ReCaptcha
    captcha = ReCaptchaField(widget=ReCaptchaV3, label='')

    class Meta:
        model = models.Message
        fields = ('customer_name',
                  'customer_email',
                  'message_text')
