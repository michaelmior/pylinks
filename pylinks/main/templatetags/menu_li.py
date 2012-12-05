from django.template import Library
from django.template.defaulttags import URLNode, url
from django.utils.html import escape, mark_safe

register = Library()


class MenuLINode(URLNode):
    def render(self, context):
        # Pull out the match and hijack asvar
        # to be used for the link title
        match = getattr(context.get('request'), 'resolver_match', None)
        if self.asvar:
            title = escape(self.asvar.strip('"\''))
        elif match:
            title = match.url_name

        # Reset asvar and render to get the URL
        self.asvar = None
        menu_url = super(MenuLINode, self).render(context)

        # Check if we're on the defined page
        if match and str(self.view_name).strip('"\'') == match.url_name:
            active_class = ' class="active"'
        else:
            active_class = ''

        return mark_safe('<li%s><a href="%s">%s</a></li>' % \
                (active_class, menu_url, title))


@register.tag
def menu_li(parser, token, node_cls=MenuLINode):
    """
    Add a menu <li> for Twitter Bootstrap, checking
    adding the "active" class as needed.
    """
    node_instance = url(parser, token)
    return node_cls(view_name=node_instance.view_name,
        args=node_instance.args,
        kwargs=node_instance.kwargs,
        asvar=node_instance.asvar)
