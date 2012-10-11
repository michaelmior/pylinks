from pylinks.main.decorators import render_to
from pylinks.links.models import Category


@render_to('index.htm')
def index(request):
    return {'categories': Category.objects.all()}
