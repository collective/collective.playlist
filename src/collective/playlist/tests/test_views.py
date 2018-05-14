# coding: utf-8
from collective.playlist.testing import COLLECTIVE_PLAYLIST_INTEGRATION_TESTING  # noqa
from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID

import unittest


class PlaylistIntegrationTest(unittest.TestCase):

    layer = COLLECTIVE_PLAYLIST_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        setRoles(self.portal, TEST_USER_ID, ['Manager'])

    def test_BaseView(self):
        view = self.portal.playlist.restrictedTraverse('@@playlistfooterview')
        tracks = [{u'mp3':
            u'http://nohost/plone/playlist/track-1/@@download/audiofile/track-1.mp3', # noqa: 128
            'title': 'Track 1'},
            {u'mp3':
            u'http://nohost/plone/playlist/track-2/@@download/audiofile/track-2.mp3', # noqa: 128
            'title': 'Track 2'},
            {u'mp3':
            u'http://nohost/plone/playlist/track-3/@@download/audiofile/track-3.mp3', # noqa: 128
            'title': 'Track 3'}]
        self.assertEqual(view.getTracks(), tracks)
        self.assertEqual(view.css_stylesheets_collectiveplaylist(), u'')
        self.assertEqual(view.getSiteLogo(), None)
        self.assertEqual(view.copyright(), u'')

    def test_EditPopupPlayer(self):
        setRoles(self.portal, TEST_USER_ID, ['Editor'])
        view = self.portal.playlist.restrictedTraverse('@@playlistfooterview')
        self.assertEqual(view.can_add_and_edit(), True)
