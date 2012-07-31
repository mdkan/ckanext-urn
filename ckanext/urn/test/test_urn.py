'''
Tests for URN generation 
'''
import logging
from ckan.model import Package, Resource, Session
import ckan.model as model
from ckan.tests import CreateTestData
from ckan.tests.functional.base import FunctionalTestCase
from ckanext.urn.plugin import generate_uuid_urn, generate_nbn_urn, get_remote_urn
import datetime
import mock
from ckan.lib.helpers import url_for

import ckanext.urn.plugin

log = logging.getLogger(__file__)

class TestURN(FunctionalTestCase):

    @classmethod
    def setup_class(cls):
        """
        Remove any initial sessions.
        """
        Session.remove()
        # TODO: Should also remove test data
        CreateTestData.create()

    @classmethod
    def teardown_class(cls):
        """
        Tear down, remove the session.
        """
        CreateTestData.delete()
        Session.remove()


    def test_urn_uuid_for_pkg(self):
        package = 'annakarenina'
        pkg = Package.by_name(package)
        urn = generate_uuid_urn(pkg)
        assert urn != ''
        assert urn.startswith('urn:')
        assert urn == 'urn:UUID:' + pkg.id

    def test_urn_nbn_for_pkg(self):
        package = 'annakarenina'
        pkg = Package.by_name(package)
        urn = generate_nbn_urn(pkg)
        assert urn != ''
        assert urn.startswith('urn:')
        assert urn.startswith('urn:NBN:')
        year_rand = urn.split('-')[-1][2:]
        assert year_rand.isdigit() == True
        year = year_rand[0:4]
        rand = year_rand[4:]
        now = datetime.datetime.now()
        assert year == str(now.year)
        assert rand.isdigit()

    def test_remote_urn(self):
        get_remote_urn = mock.Mock(return_value="URN:NBN:fi-fe201206065785")
        urn = get_remote_urn()
        assert urn != ''
        assert urn.startswith('URN:')
        assert urn.startswith('URN:NBN:')
        year_rand = urn.split('-')[-1][2:]
        assert year_rand.isdigit() == True
        year = year_rand[0:4]
        rand = year_rand[4:]
        now = datetime.datetime.now()
        assert year == str(now.year)
        assert rand.isdigit()

    def test_dataset_urn(self):
        rev = model.repo.new_revision()
        ckanext.urn.plugin.get_remote_urn = mock.Mock(return_value="URN:NBN:fi-fe201206065785")
        pkg = Package(name="test")
        Session.add(pkg)
        Session.commit()
        urn = pkg.id
        log.debug(pkg.id)
        assert urn != ''
        assert urn.startswith('URN:')
        assert urn.startswith('URN:NBN:')
        year_rand = urn.split('-')[-1][2:]
        assert year_rand.isdigit() == True
        year = year_rand[0:4]
        rand = year_rand[4:]
        now = datetime.datetime.now()
        assert year == str(now.year)
        assert rand.isdigit()
