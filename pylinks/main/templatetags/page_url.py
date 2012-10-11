from django import template
from django.core.urlresolvers import reverse, NoReverseMatch

register = template.Library()


@register.simple_tag(takes_context=True)
def page_url(context, page):
    """
    Returns the current URL paginated at a given page.
    If 'page' is accepted as a keyword argument, that
    will be used, otherwise the page will be placed in
    the query string.

    Requires Django 1.5+ and the request context processor
    """
    match = context['request'].resolver_match

    url_kwargs = match.kwargs
    url_kwargs['page'] = page

    try:
        return reverse(match.url_name, args=match.args, kwargs=url_kwargs)
    except NoReverseMatch:
        del url_kwargs['page']
        url = reverse(match.url_name, args=match.args, kwargs=url_kwargs)
        get = context['request'].GET.copy()
        get['page'] = page

        return url + '?' + get.urlencode()
