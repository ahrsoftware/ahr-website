from django.db import models
from . import apps


class Message(models.Model):
    """
    A message sent to the business by a prospective client through the website
    """

    customer_name = models.CharField(max_length=255)
    customer_email = models.EmailField()
    customer_phone = models.CharField(max_length=50, blank=True, null=True)
    message_text = models.TextField(blank=True, null=True)

    # Many to many relationships
    related_name = "message"
    service = models.ManyToManyField("Service", related_name=related_name, blank=True, db_table="{}_m2m_message_service".format(apps.app_name))

    # Admin fields
    admin_notes = models.TextField(blank=True, null=True)

    # Metadata fields
    meta_created_datetime = models.DateTimeField(auto_now_add=True, verbose_name="Created")
    meta_lastupdated_datetime = models.DateTimeField(auto_now=True, verbose_name='Last Updated')

    def __str__(self):
        created = self.meta_created_datetime.strftime("%d %b %Y %I:%M%p")
        return f"Message from {self.customer_name} ({created})"
    
    @property
    def message_text_short(self):
        return self.message_text[0:75]

    class Meta:
        ordering = ['-meta_created_datetime', '-id']


class Project(models.Model):
    """
    A project to be featured in the portfolio
    """

    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    main_image = models.ImageField(upload_to='projects', blank=True, null=True)
    link = models.URLField(blank=True, null=True)
    order = models.IntegerField(default=100)

    # Admin fields
    admin_published = models.BooleanField(default=True)
    admin_notes = models.TextField(blank=True, null=True)

    # Metadata fields
    meta_created_datetime = models.DateTimeField(auto_now_add=True, verbose_name="Created")
    meta_lastupdated_datetime = models.DateTimeField(auto_now=True, verbose_name='Last Updated')

    def __str__(self):
        return self.name

    @property
    def description_short(self):
        return self.description[0:75]

    class Meta:
        ordering = ['order', 'name', '-id']


class Service(models.Model):
    """
    A service available to customers by the business
    """

    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    fontawesome_icon = models.CharField(max_length=100, blank=True, null=True)
    order = models.IntegerField(default=100)

    # Admin fields
    admin_published = models.BooleanField(default=True)
    admin_notes = models.TextField(blank=True, null=True)

    # Metadata fields
    meta_created_datetime = models.DateTimeField(auto_now_add=True, verbose_name="Created")
    meta_lastupdated_datetime = models.DateTimeField(auto_now=True, verbose_name='Last Updated')

    def __str__(self):
        return self.name
    
    @property
    def description_short(self):
        return self.description[0:75]

    class Meta:
        ordering = ['order', 'name', '-id']
