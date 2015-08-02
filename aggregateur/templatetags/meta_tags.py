# Accès aux settings dans les templates

from django import template
from django.conf import settings

register = template.Library()

@register.simple_tag
def from_settings(name): return getattr(settings, name, "")
# {% from_settings "IMPORT_JQUERY" %}
# StackOverflow 433162