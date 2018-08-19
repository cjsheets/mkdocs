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

debug_attr_fmt = '''name:  %s
type:  %r
value: %r'''

def debugObj(value):
    begin = "<pre class='debug'>\n"
    end = "\n</pre>"

    result = ["{% filter escape %}"]
    for attr_name in dir(value):
        if attr_name[0] == "_":
            continue
        a = getattr(value, attr_name)
        result.append(debug_attr_fmt % (attr_name, type(a), a))
    result.append("{% endfilter %} ")
    tmpl = Environment().from_string("\n\n".join(result))

    return begin + tmpl.render() + end

def debugMembers(obj):
    pprint.pprint(getmembers(obj))
    return ''

@jinja2.contextfilter
def url_filter(context, value):
    """ A Template filter to normalize URLs. """
    return normalize_url(value, page=context['page'], base=context['base_url'])
