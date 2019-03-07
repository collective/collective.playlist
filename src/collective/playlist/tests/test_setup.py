# -*- coding: utf-8 -*-
"""Setup tests for this package."""
from collective.playlist.testing import COLLECTIVE_PLAYLIST_INTEGRATION_TESTING  # noqa
from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID

import unittest

try:
    from Products.CMFPlone.utils import get_installer
except ImportError:
    # BBB for Plone 5.0 and lower.
    get_installer = None

PROJECTNAME = 'collective.playlist'


class TestSetup(unittest.TestCase):
    """Test that collective.playlist is properly installed."""

    layer = COLLECTIVE_PLAYLIST_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        if get_installer is None:
            self.installer = self.portal['portal_quickinstaller']
        else:
            self.installer = get_installer(self.portal)

    def test_product_installed(self):
        self.assertTrue(self.installer.isProductInstalled(PROJECTNAME))

    def test_browserlayer(self):
        """Test that ICollectivePlaylistLayer is registered."""
        from collective.playlist.interfaces import (
            ICollectivePlaylistLayer)
        from plone.browserlayer import utils
        self.assertIn(
            ICollectivePlaylistLayer,
            utils.registered_layers())


class TestUninstall(unittest.TestCase):

    layer = COLLECTIVE_PLAYLIST_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        if get_installer is None:
            self.installer = self.portal['portal_quickinstaller']
        else:
            self.installer = get_installer(self.portal)
        setRoles(self.portal, TEST_USER_ID, ['Site Administrator'])

        self.installer.uninstallProducts(['collective.playlist'])

    def test_product_uninstalled(self):
        """Test if collective.playlist is cleanly uninstalled."""
        self.assertFalse(self.installer.isProductInstalled(
            'collective.playlist'))

    def test_browserlayer_removed(self):
        """Test that ICollectivePlaylistLayer is removed."""
        from collective.playlist.interfaces import \
            ICollectivePlaylistLayer
        from plone.browserlayer import utils
        self.assertNotIn(
            ICollectivePlaylistLayer,
            utils.registered_layers())
