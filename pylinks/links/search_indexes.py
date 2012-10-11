from haystack import indexes
from pylinks.links.models import Link


class LinkIndex(indexes.RealTimeSearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)

    def get_model(self):
        return Link
