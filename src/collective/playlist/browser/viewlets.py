from time import time
from plone.app.layout.viewlets import common as base

# from plone.memoize import forever
# from plone.memoize.instance import memoize
# from plone.memoize.view import memoize, memoize_contextless
from plone.memoize import ram

from plone import api

from Products.CMFCore.utils import getToolByName

import logging
logger = logging.getLogger(__name__)


class PlaylistViewlet(base.ViewletBase):
    """
    """

    @ram.cache(lambda *args: time() // 60)
    def _playlists(self):
        catalog = getToolByName(self.context, 'portal_catalog')
        items = catalog(portal_type='playlist', sort_on="effective", sort_order="reverse")
        return list(items)

    @ram.cache(lambda *args: time() // 60)
    def show(self):
        playlists = self._playlists()
        # print "playlists", [item.id for item in playlists]
        return playlists!=[]
        
    @ram.cache(lambda *args: time() // 1)
    def href(self):
        result = self._playlists()[0].getObject().absolute_url()
        print "url", result
        return result
        