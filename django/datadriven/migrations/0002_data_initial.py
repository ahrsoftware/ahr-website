from django.db import migrations
from datadriven import models


def insert_projects(apps, schema_editor):
    """
    Inserts Project objects
    """

    projects = [
        {
            'name': 'LINGUINDIC',
            'image': 'portfolio/linguindic.jpg',
            'link': 'https://linguindic.com/',
            'order': 1
        },
        {
            'name': 'Everyday Lookism',
            'image': 'portfolio/everydaylookism.jpg',
            'link': 'https://everydaylookism.bham.ac.uk/',
            'order': 2
        },
        {
            'name': 'Linguistic Atlas of Judeo-Spanishes',
            'image': 'portfolio/judeospanish.jpg',
            'link': 'https://judeospanish.bham.ac.uk/',
            'order': 3
        },
        {
            'name': 'Testimony in Practice',
            'image': 'portfolio/testimonyinpractice.jpg',
            'link': 'https://testimonyinpractice.bham.ac.uk/',
            'order': 4
        },
        {
            'name': 'Visualise Baudelaire Song',
            'image': 'portfolio/visualisebaudelairesong.jpg',
            'link': 'https://visualisebaudelairesong.bham.ac.uk/',
            'order': 5
        },
        {
            'name': 'Out of Our Minds',
            'image': 'portfolio/outofourminds.jpg',
            'link': 'https://outofourminds.bham.ac.uk/',
            'order': 6
        },
        {
            'name': 'Everything to Everybody',
            'image': 'portfolio/everythingtoeverybody.jpg',
            'link': 'https://everythingtoeverybody.bham.ac.uk/',
            'order': 7
        },
        {
            'name': 'CLiC Calendar',
            'image': 'portfolio/cliccalendar.jpg',
            'link': 'https://cliccalendar.bham.ac.uk/',
            'order': 8
        },
        {
            'name': 'Centre of Digital Cultures',
            'image': 'portfolio/digitalcultures.jpg',
            'link': 'https://digitalcultures.bham.ac.uk/',
            'order': 9
        },
        {
            'name': 'Post-Socialist Britain',
            'image': 'portfolio/postsocialistbritain.jpg',
            'link': 'https://postsocialistbritain.bham.ac.uk/',
            'order': 10
        },
    ]

    # Loop through above data structure, adding each item as a model
    for p in projects:
        models.Project(name=p['name'],
                       image=p['image'],
                       link=p['link'],
                       order=p['order']).save()


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
            'name': 'Visualisations',
            'fontawesome_icon': 'fas fa-chart-pie',
            'description': "Data visualisations are an extremely engaging \
                            way to read, understand, and share your data. \
                            We can design interactive visualisations and \
                            embed them in a website or mobile app.",
            'order': 4
        },
        {
            'name': 'Data Collection',
            'fontawesome_icon': 'fas fa-keyboard',
            'description': "We use software to improve the quantity and \
                            quality of the research data you collect. \
                            We can scrape large amounts of data from the web \
                            and gather high-quality responses from custom \
                            web and mobile surveys.",
            'order': 5
        },
        {
            'name': 'Data Storage',
            'fontawesome_icon': 'fas fa-database',
            'description': "We can determine the most appropriate way to \
                            store your data, whether it's as a SQL database \
                            or in a format like XML, JSON, or CSV. \
                            We'll help you design an efficient data \
                            structure and help you store your data securely.",
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
            'name': 'Branding',
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
        migrations.RunPython(insert_projects),
        migrations.RunPython(insert_services),
    ]
