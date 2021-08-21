from django.db import migrations
from datadriven import models


def insert_services(apps, schema_editor):
    """
    Inserts Service objects
    """

    services = [
        {
            'name': 'Advice',
            'fontawesome_icon': 'fas fa-comments',
            'description': "We offer free advice about lots of things \
                            and more stuff",
            'order': 1
        },
        {
            'name': 'Websites',
            'fontawesome_icon': 'fas fa-desktop',
            'description': "x \
                            x",
            'order': 2
        },
        {
            'name': 'Mobile Apps',
            'fontawesome_icon': 'fas fa-mobile-alt',
            'description': "x \
                            x",
            'order': 3
        },
        {
            'name': 'Data Collection',
            'fontawesome_icon': 'fas fa-keyboard',
            'description': "x \
                            x",
            'order': 4
        },
        {
            'name': 'Data Storage',
            'fontawesome_icon': 'fas fa-database',
            'description': "x \
                            x",
            'order': 5
        },
        {
            'name': 'Data Visualisations',
            'fontawesome_icon': 'fas fa-chart-pie',
            'description': "x \
                            x",
            'order': 6
        },
        {
            'name': 'Data Quality',
            'fontawesome_icon': 'fas fa-project-diagram',
            'description': "x \
                            x",
            'order': 7
        },
        {
            'name': 'Project Branding',
            'fontawesome_icon': 'fas fa-palette',
            'description': "x \
                            x",
            'order': 8
        },
    ]

    # Loop through above data structure, adding each item as a model
    for s in services:
        models.Service(name=s['name'],
                       fontawesome_icon=s['fontawesome_icon'],
                       description=s['description'],
                       order=s['order']).save()



class Migration(migrations.Migration):

    dependencies = [
        ('datadriven', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(insert_services),
    ]
