import json
import jinja2
import pprint
from inspect import getmembers

from mkdocs.utils import normalize_url


def tojson(obj, **kwargs):
    return jinja2.Markup(json.dumps(obj, **kwargs))


def debug(str):
    print str
    return ''


def debugObj(obj):
    pprint.pprint(obj)
    return ''

def debugMembers(obj):
    pprint.pprint(getmembers(obj))
    return ''

@jinja2.contextfilter
def url_filter(context, value):
    """ A Template filter to normalize URLs. """
    return normalize_url(value, page=context['page'], base=context['base_url'])
