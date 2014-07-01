from linkcheck import Linklist
from pylinks.links.models import Link

class LinkLinklist(Linklist):
    """ Class to let linkcheck app discover fields containing links """
    model = Link
    object_filter = {}
    url_fields = ['url']

linklists = {'Links': LinkLinklist}
