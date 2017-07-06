from django import template
from django.conf import settings
from django.utils.html import escape, mark_safe

register = template.Library()


@register.simple_tag(takes_context=True)
def analytics(context):
    if not getattr(settings, 'GA_PROPERTY_ID', None):
        return ''

    return mark_safe('''
        <script type="text/javascript">
          var _gaq = _gaq || [];
          _gaq.push(['_setAccount', '%s']);
          _gaq.push(['_trackPageview']);

          (function() {
            var ga = document.createElement('script'); ga.type = 'text/javascript'; ga.async = true;
            ga.src = ('https:' == document.location.protocol ? 'https://ssl' : 'http://www') + '.google-analytics.com/ga.js';
            var s = document.getElementsByTagName('script')[0]; s.parentNode.insertBefore(ga, s);
          })();
        </script>
        ''' % escape(settings.GA_PROPERTY_ID))
