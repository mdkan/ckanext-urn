from ckan.controllers.package import PackageController
from ckan.lib.base import c
from pylons import url
import logging

log = logging.getLogger(__name__)

class URNResourceController(PackageController):
    def editresources(self, id, data=None, errors=None, error_summary=None):
        c.action = 'editresources'
        routes_dict = url.environ['pylons.routes_dict']
        routes_dict['controller'] = 'package'
        form = super(URNResourceController, self).editresources(id,data,errors,error_summary)
        log.debug(form)
        return form