from pylinks.main.decorators import render_to
from pylinks.links.models import Category


@render_to('category_index.htm')
def category_index(request):
    return {'categories': Category.objects.all()}

@render_to('alpha_index.htm')
def alpha_index(request):
    return {}
