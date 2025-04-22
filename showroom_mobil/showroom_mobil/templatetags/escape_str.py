from django import template
import logging

logger = logging.getLogger(__name__)
register = template.Library()

@register.filter(name='escapejstr')
def escapejs(value):
    if isinstance(value, str):
        return value.replace("'", "\\'").replace('"', '\\"').replace("\\", "\\\\")
    return value
