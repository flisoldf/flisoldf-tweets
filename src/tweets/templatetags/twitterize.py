try:
    from django.template import Library
    from django.template.defaultfilters import stringfilter
except:
    raise Exception('Django is not installed.')

# Ivens Rocha - abril/2012
# datetime and email needed to make to_datetime work
from datetime import datetime, timedelta
from email.utils import parsedate_tz

from twitter_text import TwitterText

register = Library()

@register.filter(name = 'twitter_text')
@stringfilter
def twitter_text(text, search_query = False):
    """
    Parses a text string through the TwitterText auto_link method and if search_query is passed, through the hit_highlight method.
    """
    tt = TwitterText(text)
    if search_query:
        tt.highlighter.hit_highlight(search_query)
    tt.autolink.auto_link()
    return tt.text
twitter_text.is_safe = True


@register.filter(name = 'twitter_datetime')
def to_datetime(datestring):
    datestring = datestring[:-5] + "+0300"
    time_tuple = parsedate_tz(datestring.strip())
    dt = datetime(*time_tuple[:6])
    return dt - timedelta(seconds=time_tuple[-1])