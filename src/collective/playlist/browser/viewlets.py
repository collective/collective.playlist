# coding: utf-8
from plone import api
from plone.app.layout.viewlets import common as base

import logging


logger = logging.getLogger(__name__)


class PlaylistButtonViewlet(base.ViewletBase):
    """
    """

    def _playlists(self):
        """Anonymous gets only published playlists
        """
        catalog = api.portal.get_tool(name='portal_catalog')
        items = catalog(portal_type='playlist', sort_on='effective',
                        sort_order='reverse')
        return list(items)

    def show(self):
        """ Show play button only if published playlist exists
        """
        playlists = self._playlists()
        return playlists != []

    def href(self):
        result = self._playlists()[0].getObject().absolute_url()
        return result + '/@@playlistpopupview'


class PlaylistFooterViewlet(PlaylistButtonViewlet):
    """
    """

    def playlist(self):
        result = self._playlists()[0].getObject()
        return result
