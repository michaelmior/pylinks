from django.template import Library
from django.urls import reverse
from django.utils.html import escape, mark_safe

register = Library()


@register.simple_tag(takes_context=True)
def menu_li(context, url_name, title):
    menu_url = reverse(url_name)

    # Check if we're on the defined page
    if hasattr(context, "request") and context.request.path == menu_url:
        active_class = ' class="active"'
    else:
        active_class = ""

    return mark_safe(f'<li{active_class}><a href="{menu_url}">{escape(title)}</a></li>')
