# -*- coding: utf-8 -*-
"""Setup tests for this package."""
from plone import api
from collective.playlist.testing import COLLECTIVE_PLAYLIST_INTEGRATION_TESTING  # noqa

import unittest


class TestSetup(unittest.TestCase):
    """Test that collective.playlist is properly installed."""

    layer = COLLECTIVE_PLAYLIST_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')

    def test_product_installed(self):
        """Test if collective.playlist is installed."""
        self.assertTrue(self.installer.isProductInstalled(
            'collective.playlist'))

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
        self.installer = api.portal.get_tool('portal_quickinstaller')
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
