from time import time
from plone.app.layout.viewlets import common as base
from plone import api
from plone.memoize import ram
from Products.CMFCore.utils import getToolByName

import logging
logger = logging.getLogger(__name__)


class PlaylistViewlet(base.ViewletBase):
    """
    """

    @ram.cache(lambda *args: time() // 3)
    def _playlists(self):
        """Anonymous gets only published playlists
        """
        catalog = getToolByName(self.context, 'portal_catalog')
        items = catalog(portal_type='playlist', sort_on="effective", sort_order="reverse")
        return list(items)

    @ram.cache(lambda *args: time() // 3)
    def show(self):
        """ Show play button only if published playlist exists
        """        
        playlists = self._playlists()
        return playlists!=[]
        
    @ram.cache(lambda *args: time() // 3)
    def href(self):
        result = self._playlists()[0].getObject().absolute_url()
        return result
        