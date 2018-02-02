from plone.memoize.view import memoize
from plone import api
from Products.CMFPlone.resources import add_resource_on_request

from plone.dexterity.browser.view import DefaultView

import logging
logger = logging.getLogger(__name__)

from collective.playlist import _


class PlaylistView(DefaultView):
    """
    """
        
    def dict_tracks(self):
        """ {
            title:"Your Face",
            mp3:"http://www.jplayer.org/audio/mp3/TSP-05-Your_face.mp3",
            oga:"http://www.jplayer.org/audio/ogg/TSP-05-Your_face.ogg"
        }
        """
        
        context = self.context
        
        # brains = self.context.getFolderContents()
        items = context.contentItems()
        tracks = [item for item in items if item[1].portal_type=="track"]
        tracklist = ""
        for tr in tracks:
            title = tr[1].title
            format = tr[1].audiofile.filename.split(".")[-1]
            address = "/".join([context.absolute_url(), tr[0], "@@download/audiofile", tr[1].audiofile.filename])
            str = "{{title:'{title}', {format}:'{address}'}}".format(title=title, format=format, address=address)
            tracklist += str + ", "
        return tracklist
            
    def js_collectiveplaylist(self):
        js = """ $(document).ready(function(){{

    new jPlayerPlaylist({{
        jPlayer: "#jquery_jplayer_playlist",
        cssSelectorAncestor: "#jp_container_playlist"
    }}, [ {dtracks}
    ], {{
        volume: 1.0,
        playlistOptions: {{
            autoPlay: false,}},
        swfPath: "../../dist/jplayer",
        supplied: "oga, ogg, mp3, wav",
        wmode: "window",
        useStateClassSkin: true,
        autoBlur: false,
        smoothPlayBar: true,
        keyEnabled: true
    }});


}});"""
        return js.format(dtracks=self.dict_tracks())
    
    
    def can_add_and_edit(self):
        # TODO: check Playlist admin-Menu for roles
        roles = api.user.get_roles()
        result = "Manager" in roles or "Site Administrator" in roles or "Editor" in roles
        return result
        
        return True