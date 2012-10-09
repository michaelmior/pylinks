from django import template
from django.core.urlresolvers import reverse

register = template.Library()


@register.simple_tag(takes_context=True)
def self_url(context, *args, **kwargs):
    """
    Returns the URL for the current page with updated
    arguments. If positional arguments are omitted,
    the arguments passed to the view as rendered are used.

    Requires Django 1.5+ and the request context processor
    """
    match = context['request'].resolver_match

    url_args = args or match.args
    url_kwargs = match.kwargs
    url_kwargs.update(kwargs)

    return reverse(match.url_name, args=url_args, kwargs=url_kwargs)
