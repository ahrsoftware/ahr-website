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
                                      help_text='Optional',
                                      required=False)
    customer_phone = forms.CharField(label=_('Phone'),
                                     help_text='Optional',
                                     required=False)
    message_text = forms.CharField(widget=forms.Textarea(attrs={'rows': 4}),
                                   label=_('Message'))
    service = forms.ModelMultipleChoiceField(label=_("Services I'd like to discuss"),
                                             queryset=models.Service.objects,
                                             widget=forms.CheckboxSelectMultiple,
                                             help_text=_('Optional. Select all that apply'),
                                             required=False)

    # Google ReCaptcha
    captcha = ReCaptchaField(widget=ReCaptchaV3, label='')

    class Meta:
        model = models.Message
        fields = ('customer_name',
                  'customer_email',
                  'customer_phone',
                  'message_text',
                  'service')
