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
            'description': "We offer free, no-obligation advice sessions \
                            where we discuss how software and data can \
                            play a vital role in your research project.",
            'order': 1
        },
        {
            'name': 'Websites',
            'fontawesome_icon': 'fas fa-desktop',
            'description': "We build bespoke, advanced websites to \
                            collect, store, and present your research data. \
                            We can design, develop, host, and maintain your \
                            website throughout the lifetime of your project.",
            'order': 2
        },
        {
            'name': 'Mobile Apps',
            'fontawesome_icon': 'fas fa-mobile-alt',
            'description': "We develop beautiful mobile apps for both \
                            Android and iOS devices to deliver an engaging and \
                            impactful experience for your research participants.",
            'order': 3
        },
        {
            'name': 'Data Collection',
            'fontawesome_icon': 'fas fa-keyboard',
            'description': "We use software to improve the quantity and \
                            quality of the research data you collect. \
                            We can scrape large amounts of data from the web \
                            and gather high-quality responses from custom web surveys.",
            'order': 4
        },
        {
            'name': 'Data Storage',
            'fontawesome_icon': 'fas fa-database',
            'description': "We can determine the most appropriate way to \
                            store your data, whether it's as a SQL database \
                            or in a format like XML, JSON, or CSV. \
                            We'll help you design an efficient data \
                            structure and help you store your data securely.",
            'order': 5
        },
        {
            'name': 'Data Visualisations',
            'fontawesome_icon': 'fas fa-chart-pie',
            'description': "Data visualisations are an extremely engaging \
                            way to read, understand, and share your data. \
                            We can design interactive visualisations and \
                            embed them in a website or mobile app.",
            'order': 6
        },
        {
            'name': 'Data Quality',
            'fontawesome_icon': 'fas fa-project-diagram',
            'description': "We can write software to automatically detect \
                            inconsistencies and errors in your data, leading to \
                            higher quality data and more accurate research outputs.",
            'order': 7
        },
        {
            'name': 'Project Branding',
            'fontawesome_icon': 'fas fa-palette',
            'description': "We can design unique and attractive branding \
                            for your research project and apply this to your \
                            project website to make a consistent and professional \
                            impression on your audience.",
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
