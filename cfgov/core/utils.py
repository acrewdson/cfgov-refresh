import re
from six import text_type as str
from six.moves.urllib.parse import parse_qs, urlencode, urlparse

import django
from django.core.signing import Signer
from django.core.urlresolvers import reverse

from bs4 import BeautifulSoup, NavigableString

from core.templatetags.svg_icon import svg_icon


NON_GOV_LINKS = re.compile(
    r'https?:\/\/(?:www\.)?(?![^\?]+gov)(?!(content\.)?localhost).*'
)
NON_CFPB_LINKS = re.compile(
    r'(https?:\/\/(?:www\.)?(?![^\?]*(cfpb|consumerfinance).gov)'
    '(?!(content\.)?localhost).*)'
)
DOWNLOAD_LINKS = re.compile(
    r'(?i)(\.pdf|\.doc|\.docx|\.xls|\.xlsx|\.csv|\.zip)$'
)
LINK_ICON_CLASSES = 'a-link a-link__icon'

LINK_ICON_TEXT_CLASSES = 'a-link_text'


def append_query_args_to_url(base_url, args_dict):
    return "{0}?{1}".format(base_url, urlencode(args_dict))


def sign_url(url, secret=None):
    if secret:
        signer = Signer(secret, sep='||')
    else:
        signer = Signer(sep='||')

    url, signature = signer.sign(url).split('||')
    return (url, signature)


def signed_redirect(url):
    url, signature = sign_url(url)
    query_args = {'ext_url': url,
                  'signature': signature}

    return ('{0}?{1}'.format(reverse('external-site'), urlencode(query_args)))


def unsigned_redirect(url):
    query_args = {'ext_url': url}
    return ('{0}?{1}'.format(reverse('external-site'), urlencode(query_args)))


def extract_answers_from_request(request):
    answers = [(param.split('_')[1], value) for param, value in
               request.POST.items() if param.startswith('questionid')]
    return sorted(answers)


def format_file_size(bytecount, suffix='B'):
    """Convert a byte count into a rounded human-friendly file size."""
    for unit in ['', 'K', 'M', 'G']:
        if abs(bytecount) < 1024.0:
            return "{:1.0f} {}{}".format(bytecount, unit, suffix)
        bytecount /= 1024.0
    return "{:.0f} {}{}".format(bytecount, 'T', suffix)


def get_link_tags(soup):
    tags = []
    for a in soup.find_all('a', href=True):
        if not is_image_tag(a):
            tags.append(a)
    return tags


def is_image_tag(tag):
    for child in tag.children:
        if child.name in ['img', 'svg']:
            return True
    return False


def add_link_markup(tag):
    """Add necessary markup to the given link and return if modified.

    Add an external link icon if the input is not a CFPB (internal) link.
    Add an external link redirect if the input is not a gov link.
    Add a download icon if the input is a file.
    Otherwise (internal link that is not a file), return None.
    """
    icon = False

    if not tag.attrs.get('class', None):
        tag.attrs.update({'class': []})

    if tag['href'].startswith('/external-site/?'):
        # Sets the icon to indicate you're leaving consumerfinance.gov
        icon = 'external-link'
        components = urlparse(tag['href'])
        arguments = parse_qs(components.query)
        if 'ext_url' in arguments:
            external_url = arguments['ext_url'][0]
            # Add the redirect notice as well
            tag['href'] = signed_redirect(external_url)

    elif NON_CFPB_LINKS.match(tag['href']):
        # Sets the icon to indicate you're leaving consumerfinance.gov
        icon = 'external-link'
        if NON_GOV_LINKS.match(tag['href']):
            # Add the redirect notice as well
            tag['href'] = signed_redirect(tag['href'])

    elif DOWNLOAD_LINKS.search(tag['href']):
        # Sets the icon to indicate you're downloading a file
        icon = 'download'

    if icon:
        tag.attrs['class'].append(LINK_ICON_CLASSES)
        # Wraps the link text in a span that provides the underline
        contents = tag.contents
        span = BeautifulSoup('', 'html.parser').new_tag('span')
        span['class'] = LINK_ICON_TEXT_CLASSES
        span.contents = contents
        tag.contents = [span, NavigableString(' ')]
        # Appends the SVG icon
        tag.contents.append(BeautifulSoup(svg_icon(icon), 'html.parser'))
        return str(tag)

    return None


class NoMigrations(object):
    """Class to disable app migrations through settings.MIGRATION_MODULES.

    The MIGRATION_MODULES setting can be used to tell Django where to look
    for an app's migrations (by default this is the "migrations" subdirectory).
    This class simulates a dictionary where a lookup for any app returns a
    value that causes Django to think that no migrations exist.

    In Django >= 1.9, this can be configured by returning None. In Django <1.9,
    a nonexistent path string must be returned.
    """
    def __contains__(self, item):
        return True

    def __getitem__(self, item):
        if django.VERSION[:2] < (1, 9):  # pragma: no cover
            return 'nomigrations'
        else:
            return None
