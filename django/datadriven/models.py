from django.db import models


class Project(models.Model):
    """
    A project to be featured in the portfolio
    """

    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    main_image = models.ImageField(upload_to='projects', blank=True, null=True)
    link = models.URLField(blank=True, null=True)

    # Admin fields
    admin_published = models.BooleanField(default=False)
    admin_notes = models.TextField(blank=True, null=True)

    # Metadata fields
    meta_created_datetime = models.DateTimeField(auto_now_add=True, verbose_name="Created")
    meta_lastupdated_datetime = models.DateTimeField(auto_now=True, verbose_name='Last Updated')

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name', '-id']


class Service(models.Model):
    """
    A service available to customers by the business
    """

    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    icon = models.CharField(blank=True, null=True)

    # Admin fields
    admin_published = models.BooleanField(default=False)
    admin_notes = models.TextField(blank=True, null=True)

    # Metadata fields
    meta_created_datetime = models.DateTimeField(auto_now_add=True, verbose_name="Created")
    meta_lastupdated_datetime = models.DateTimeField(auto_now=True, verbose_name='Last Updated')

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name', '-id']
