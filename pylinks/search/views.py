from django.http import Http404
from django.core.paginator import Paginator, InvalidPage
from django.utils.translation import ugettext as _
from haystack.views import SearchView


class SearchView(SearchView):
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
        return {'is_paginated': bool(self.query)}
