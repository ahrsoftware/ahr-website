from django.contrib import admin
import datetime
from . import models


def publish(modeladmin, request, queryset):
    """
    Sets all selected items in queryset to published
    """
    queryset.update(admin_published=True)


publish.short_description = "Publish selected items (will appear on main site)"


def unpublish(modeladmin, request, queryset):
    """
    Sets all selected items in queryset to not published
    """
    queryset.update(admin_published=False)


unpublish.short_description = "Unpublish selected items (will not appear on main site)"


class ProjectAdminView(admin.ModelAdmin):
    """
    Admin for the Project model
    """
    list_display = ('id', 'name', 'link', 'admin_published', 'meta_created_datetime')
    list_display_links = ('id', 'name')
    list_filter = ('admin_published', 'meta_created_by')
    search_fields = ('name', 'description', 'link', 'admin_notes')
    ordering = ('id',)
    actions = (publish, unpublish)
    readonly_fields = ('meta_created_by', 'meta_created_datetime', 'meta_lastupdated_by', 'meta_lastupdated_datetime', 'meta_firstpublished_datetime')

    def save_model(self, request, obj, form, change):
        """
        Override default save_model, by adding values to automated fields
        """

        # Meta: created by
        if getattr(obj, 'meta_created_by', None) is None:
            obj.meta_created_by = request.user
        # Meta: last updated by
            obj.meta_lastupdated_by = request.user
        # Meta: first published datetime (only set if the first time being published)
        if getattr(obj, 'admin_published', None) is True and getattr(obj, 'meta_firstpublished_datetime', None) is None:
            obj.meta_firstpublished_datetime = datetime.datetime.now()
        # Save
        obj.save()


admin.site.register(models.Project, ProjectAdminView)
