from django.contrib import admin
from . import models

# Set the title of the dashboard
admin.site.site_header = 'AHR Software: Admin Dashboard'


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


class MessageAdminView(admin.ModelAdmin):
    """
    Admin for the Message model
    """
    list_display = ('id', 'meta_created_datetime', 'customer_name', 'customer_email', 'message_text_short')
    list_display_links = ('id', 'meta_created_datetime')
    search_fields = ('customer_name', 'customer_email', 'message_text' 'admin_notes')
    readonly_fields = ('meta_created_datetime', 'meta_lastupdated_datetime')


class ProjectAdminView(admin.ModelAdmin):
    """
    Admin for the Project model
    """
    list_display = ('id', 'name', 'order', 'description_short', 'link', 'admin_published', 'meta_created_datetime')
    list_display_links = ('id', 'name')
    list_filter = ('admin_published',)
    search_fields = ('name', 'description', 'link', 'admin_notes')
    ordering = ('order', 'name', 'id')
    actions = (publish, unpublish)
    readonly_fields = ('meta_created_datetime', 'meta_lastupdated_datetime')


class ServiceAdminView(admin.ModelAdmin):
    """
    Admin for the Service model
    """
    list_display = ('id', 'name', 'order', 'description_short', 'fontawesome_icon', 'admin_published', 'meta_created_datetime')
    list_display_links = ('id', 'name')
    list_filter = ('admin_published',)
    search_fields = ('name', 'description', 'fontawesome_icon', 'admin_notes')
    ordering = ('order', 'name', 'id')
    actions = (publish, unpublish)
    readonly_fields = ('meta_created_datetime', 'meta_lastupdated_datetime')


admin.site.register(models.Message, MessageAdminView)
admin.site.register(models.Project, ProjectAdminView)
admin.site.register(models.Service, ServiceAdminView)
