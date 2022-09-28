from haystack import indexes

from pylinks.links.models import Link


class LinkIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    title = indexes.CharField(model_attr="title", boost=1.125)

    def get_model(self):
        return Link
