from linkcheck import Linklist
from .models import Link


class ExternalLinkList(Linklist):
    model = Link
    url_fields = ['url']
    ignore_empty = ['url']

linklists = {'Links': ExternalLinkList}
