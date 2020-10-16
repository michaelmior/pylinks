import string

from pylinks.links.models import Category, Link
from pylinks.main.decorators import render_to


@render_to('category_index.htm')
def category_index(request):
    return {'categories': Category.objects.all()}

@render_to('alpha_index.htm')
def alpha_index(request):
    letters = {}
    for letter in string.uppercase:
        count = Link.objects.filter(title__istartswith=letter).count()
        letters[letter] = count

    return { 'letters': letters }
