from django.shortcuts import get_object_or_404
from django.views.generic import ListView
from django.http import Http404, HttpResponseRedirect
from django.db.models import F
from pylinks.links.models import Category, Link


class LinkListView(ListView):
    model = Link
    context_object_name = 'links'
    paginate_by = 20


class CategoryListView(LinkListView):
    template_name = 'links/category.htm'

    def get(self, request, *args, **kwargs):
        # We set the category here to be used later
        self.category = get_object_or_404(Category, slug=kwargs.get('slug'))
        return super(CategoryListView, self).get(request, *args, **kwargs)

    def get_queryset(self):
        return self.category.links.all()

    def get_context_data(self, *args, **kwargs):
        # Just add the category to the context
        context = super(CategoryListView, self) \
                    .get_context_data(*args, **kwargs)

        context['category'] = self.category
        context['page'] = context['page_obj']
        del context['page_obj']

        return context


class RecentListView(LinkListView):
    template_name = 'links/recent.htm'

    def get_queryset(self):
        return Link.objects.all().order_by('-created_time')


class PopularListView(LinkListView):
    template_name = 'links/popular.htm'

    def get_queryset(self):
        return Link.objects.all().order_by('-visits')


def track_link(request, link_id):
    try:
        link = Link.objects.select_for_update().get(pk=link_id)
    except Link.DoesNotExist:
        raise Http404

    link.visits = F('visits') + 1
    link.save(update_fields=['visits'])

    if link.file:
        url = link.file.url
    else:
        url = link.url
    return HttpResponseRedirect(url)
