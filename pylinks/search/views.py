from django.core.paginator import InvalidPage, Paginator
from django.http import Http404
from django.utils.translation import ugettext as _
from haystack.forms import FacetedSearchForm
from haystack.query import SearchQuerySet
from haystack.views import FacetedSearchView


class SearchView(FacetedSearchView):
    template = 'search/search.htm'

    def __init__(self, *args, **kwargs):
        super(SearchView, self).__init__(*args, **kwargs)

        self.form_class = FacetedSearchForm
        self.searchqueryset = SearchQuerySet()

    def build_page(self):
        page = self.request.resolver_match.kwargs.get('page') or self.request.GET.get('page') or 1
        try:
            page_number = int(page)
        except ValueError:
            if page == 'last':
                page_number = paginator.num_pages
            else:
                raise Http404(_("Page is not 'last', nor can it be converted to an int."))

        paginator = Paginator(self.results, self.results_per_page)
        try:
            page = paginator.page(page_number)
        except InvalidPage:
            raise Http404(_('Invalid page (%(page_number)s)') % {
                                'page_number': page_number
            })

        return (paginator, page)

    def extra_context(self):
        context = super(SearchView, self).extra_context()
        context.update({'is_paginated': bool(self.query)})
        return context
