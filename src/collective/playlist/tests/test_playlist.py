# -*- coding: utf-8 -*-
from collective.playlist.content.playlist import IPlaylist
from collective.playlist.testing import COLLECTIVE_PLAYLIST_INTEGRATION_TESTING  # noqa
from plone import api
from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID
from plone.dexterity.interfaces import IDexterityFTI
from zope.component import createObject
from zope.component import queryUtility

import unittest


class PlaylistIntegrationTest(unittest.TestCase):

    layer = COLLECTIVE_PLAYLIST_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        setRoles(self.portal, TEST_USER_ID, ['Manager'])

    def test_schema(self):
        fti = queryUtility(IDexterityFTI, name='playlist')
        schema = fti.lookupSchema()
        self.assertEqual(IPlaylist, schema)

    def test_fti(self):
        fti = queryUtility(IDexterityFTI, name='playlist')
        self.assertTrue(fti)

    def test_factory(self):
        fti = queryUtility(IDexterityFTI, name='playlist')
        factory = fti.factory
        obj = createObject(factory)
        self.assertTrue(IPlaylist.providedBy(obj))

    def test_adding(self):
        setRoles(self.portal, TEST_USER_ID, ['Contributor'])
        obj = api.content.create(
            container=self.portal,
            type='playlist',
            id='myplaylist',
        )
        self.assertTrue(IPlaylist.providedBy(obj))
