# coding: utf-8
from collective.playlist.testing import COLLECTIVE_PLAYLIST_INTEGRATION_TESTING  # noqa
from lxml import etree
from plone import api
from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID
from Products.Five.browser import BrowserView as View
from zope.component import getMultiAdapter
from zope.viewlet.interfaces import IViewletManager

import unittest


class PlaylistButtonViewletTestCase(unittest.TestCase):

    layer = COLLECTIVE_PLAYLIST_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        self.request = self.layer['request']
        setRoles(self.portal, TEST_USER_ID, ['Manager'])
        self.workflowTool = api.portal.get_tool(name='portal_workflow')
        self.playlist = self.portal.playlist

    def toggle_playbutton(self, enable):
        """activate / deactivate viewlet"""
        view = self.portal.restrictedTraverse('@@manage-viewlets')
        if enable:
            view.show('plone.portalheader',
                      'collective.playlist.playerbuttonviewlet')
        else:
            view.hide('plone.portalheader',
                      'collective.playlist.playerbuttonviewlet')

    def get_viewlet_manager(self, context, name='plone.portalheader'):
        request = self.request
        view = View(context, request)
        manager = getMultiAdapter(
            (context, request, view), IViewletManager, name)
        return manager

    def get_viewlet(self, context,
                    name='collective.playlist.playerbuttonviewlet'):
        manager = self.get_viewlet_manager(context)
        manager.update()
        viewlet = [v for v in manager.viewlets if v.__name__ == name]
        assert len(viewlet) == 1
        return viewlet[0]

    def test_playlistbutton_enabled_disabled(self):
        self.toggle_playbutton(True)
        viewlet = self.get_viewlet(self.portal)

        html = etree.HTML(viewlet())
        a = html.xpath('//a[contains(@class,"playlist-button")]')
        self.assertEqual(len(a), 1)

        self.workflowTool.doActionFor(self.playlist, 'retract')
        setRoles(self.portal, TEST_USER_ID, ['Anonymous'])

        view = self.portal.restrictedTraverse('view')
        html = etree.HTML(view())
        a = html.xpath('//a[contains(@class,"playlist-button")]')
        self.assertEqual(len(a), 0)


class PlaylistFooterViewletTestCase(unittest.TestCase):

    layer = COLLECTIVE_PLAYLIST_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        self.request = self.layer['request']
        setRoles(self.portal, TEST_USER_ID, ['Anonymous'])

    def get_viewlet_manager(self, context, name='plone.portalfooter'):
        request = self.request
        view = View(context, request)
        manager = getMultiAdapter(
            (context, request, view), IViewletManager, name)
        return manager

    def get_viewlet(self, context,
                    name='collective.playlist.playerfooterviewlet'):
        manager = self.get_viewlet_manager(context)
        manager.update()
        viewlet = [v for v in manager.viewlets if v.__name__ == name]
        assert len(viewlet) == 1
        return viewlet[0]

    def test_footerviewlet(self):
        view = self.portal.restrictedTraverse('view')
        html = etree.HTML(view())
        player = html.xpath('//div[contains(@id,"jquery_jplayer_playlist")]')
        self.assertEqual(len(player), 1)

        viewlet = self.get_viewlet(self.portal)
        html = etree.HTML(viewlet())
        player = html.xpath('//div[contains(@id,"jquery_jplayer_playlist")]')
        self.assertEqual(len(player), 1)
        self.assertNotEqual(viewlet.playlist(), None)
