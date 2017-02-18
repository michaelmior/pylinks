from linkcheck import Linklist
from pylinks.links.models import Link

class LinkLinklist(Linklist):
    """ Class to let linkcheck app discover fields containing links """
    model = Link
    url_fields = ['url']

linklists = {'Links': LinkLinklist}
