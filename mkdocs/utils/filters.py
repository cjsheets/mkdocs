import json
import jinja2
import pprint
from inspect import getmembers

def tojson(obj, **kwargs):
    return jinja2.Markup(json.dumps(obj, **kwargs))


def debug(str):
    print str
    return ''


def debugObj(obj):
    pprint.pprint(getmembers(obj))
    return ''
