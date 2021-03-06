import logging
import os

from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from django.db import transaction

from wagtail.wagtailcore.models import Page, Site
from wagtailsharing.models import SharingSite

from v1.models import HomePage


logger = logging.getLogger(__name__)


@transaction.atomic
def run():
    logger.info('Running script initial_data')

    admin_username = 'admin'
    admin_password = 'admin'
    staging_hostname = os.environ.get('DJANGO_STAGING_HOSTNAME',
                                      'content.localhost')
    http_port = os.environ.get('DJANGO_HTTP_PORT', '80')

    # Create admin user if it doesn't exist already.
    # Update existing one with admin password and active state.
    User.objects.update_or_create(
        username=admin_username,
        defaults={
            'password': make_password(admin_password),
            'is_superuser': True,
            'is_staff': True,
            'is_active': True,
        }
    )

    # Create home page if it doesn't exist already.
    try:
        home_page = HomePage.objects.get(slug='cfgov')
    except HomePage.DoesNotExist:
        home_page = HomePage(
            title='CFGov',
            slug='cfgov',
            live=True
        )

        root_page = Page.objects.get(slug='root')
        root_page.add_child(instance=home_page)

        home_page_revision = home_page.save_revision()
        home_page_revision.publish()

    # Make sure default site (either the one installed with Wagtail, or one
    # that has since been manually setup) is running on the correct port and
    # with the expected home page as its root.
    default_site = Site.objects.get(is_default_site=True)
    default_site.hostname = 'localhost'
    default_site.port = http_port
    default_site.root_page_id = home_page.id
    default_site.save()

    # Setup a sharing site if it doesn't exist already. Use the default
    # Wagtail site.
    SharingSite.objects.update_or_create(
        site=default_site,
        defaults={
            'hostname': staging_hostname,
            'port': http_port,
        }
    )

    # Delete the legacy Wagtail "hello world" page, if it exists.
    try:
        hello_world = Page.objects.get(slug='home')
    except Page.DoesNotExist:
        pass
    else:
        hello_world.delete()
