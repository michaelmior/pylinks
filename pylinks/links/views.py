from django.shortcuts import get_object_or_404
from django.views.generic import ListView
from pylinks.links.models import Category, Link


class LinkListView(ListView):
    model = Link
    context_object_name = 'links'
    paginate_by = 20


class CategoryListView(LinkListView):
    model = Link
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
        return context


class RecentListView(LinkListView):
    model = Link
    template_name = 'links/recent.htm'

    def get_queryset(self):
        return Link.objects.all().order_by('-created_time')
