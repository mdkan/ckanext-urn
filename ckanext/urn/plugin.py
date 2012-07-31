'''
URN generation plugin for CKAN
'''
import logging
from ckan.plugins import implements, SingletonPlugin
from ckan.plugins import IMapper, IRoutes, IConfigurer
from ckan.model import Package
from pylons import config
import datetime
import random
import string
import urllib
from genshi.input import HTML
from genshi.filters import Transformer
import html

log = logging.getLogger(__name__)

class URNPlugin(SingletonPlugin):
    '''
    URN Generation plugin, activates when creating an instance of a domain
    object.
    '''
    implements(IMapper, inherit=True)
    implements(IRoutes, inherit=True)
    implements(IConfigurer, inherit=True)

    def before_insert(self, mapper, connection, instance):
        """
        Receive an object instance before that instance is INSERTed into
        its table.
        """
        if isinstance(instance, Package):
            id = get_remote_urn()
            if id:
                instance.id = id
            else:
                instance.id = "URN:UUID:%s" % instance.id

    def after_insert(self, mapper, connection, instance):
        """
        Receive an object instance after that instance is INSERTed.
        """

    def before_map(self, map):
        map.connect('/dataset/{action}/{id}',
                controller='ckanext.urn.controller:URNResourceController',
                action='editresources',
                )
        return map

    def configure(self, config):
        pass

def get_remote_urn():
    '''
    Get a URN from a url instance.
    '''
    urn_url = config.get('urn_url')
    if (urn_url):
        content = urllib.urlopen(urn_url)
        log.debug(content)
        return content.read()
    else:
        return None

def generate_uuid_urn(pkg):
    '''
    Get a URN based on a dataset UUID.
    '''
    id = pkg.id
    urn = 'urn:UUID:' + id
    pkg.urn = urn
    return urn

def generate_nbn_urn(pkg):
    '''
    Get a NBN url for library based id's.
    '''
    now = datetime.datetime.now()
    urn = 'urn:NBN:fi-fe%s%s' % (now.year, ''.join(random.choice(string.digits) \
                                                 for x in range(8)))
    pkg.urn = urn
    return urn