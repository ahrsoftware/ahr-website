from django.db import models
from django.contrib.auth.models import User


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

    meta_created_by = models.ForeignKey(User,
                                        related_name="project_created_by",
                                        on_delete=models.PROTECT,
                                        blank=True,
                                        null=True,
                                        verbose_name="Created By")
    meta_created_datetime = models.DateTimeField(auto_now_add=True, verbose_name="Created")
    meta_lastupdated_by = models.ForeignKey(User,
                                            related_name="project_lastupdated_by",
                                            on_delete=models.PROTECT,
                                            blank=True,
                                            null=True,
                                            verbose_name="Last Updated By")
    meta_lastupdated_datetime = models.DateTimeField(auto_now=True, verbose_name='Last Updated')
    meta_firstpublished_datetime = models.DateTimeField(blank=True, null=True, verbose_name="First Published")

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name', '-id']
