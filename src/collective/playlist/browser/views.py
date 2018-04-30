# coding: utf-8

import json
from collective.playlist import ALLOWED_AUDIOTYPES
from plone import api
from plone.dexterity.browser.view import DefaultView
from plone.memoize import ram
from Products.CMFPlone.resources import add_bundle_on_request
from time import time

import logging
logger = logging.getLogger(__name__)


class PlaylistView(DefaultView):
    """
    """

    def __call__(self):
        add_bundle_on_request(self.request, 'collectiveplaylist')
        add_bundle_on_request(self.request, 'jplayerplaylist')


    def _dict_tracks(self):
        """ list of track dictionaries

[{"mp3":
        "http://localhost:10680/playlisttest/playlist/track-1/@@download/audiofile/track-1.mp3",
    "title": "Track 1"},
{"mp3":
        "http://localhost:10680/playlisttest/playlist/track-2/@@download/audiofile/track-2.mp3",
    "title": "Track 2"},
{"mp3":
        "http://localhost:10680/playlisttest/playlist/track-3/@@download/audiofile/track-3.mp3",
    "title": "Track 3"}]
"""

        context = self.context
        items = context.contentItems()
        tracks = [item for item in items if (item[1].portal_type == 'track' and
                                             api.content.get_state(obj=item[1]) == 'published')]
        tracklist = []
        for tr in tracks:
            title = tr[1].title
            format = tr[1].audiofile.filename.split('.')[-1]
            format = format in ALLOWED_AUDIOTYPES and format or 'mp3'
            address = '/'.join([context.absolute_url(),
                                tr[0],
                                '@@download/audiofile',
                                tr[1].audiofile.filename])
            tracklist.append({'title': title, format: address})
        return tracklist

    # @ram.cache(lambda *args: time() // 3)
    def js_collectiveplaylist(self):
        """ Initialize JPlayer"""
        js = u""" $(document).ready(function(){{

    new jPlayerPlaylist({{
        jPlayer: "#jquery_jplayer_playlist",
        cssSelectorAncestor: "#jp_container_playlist"
    }}, {dtracks},
    {{
        volume: 0.85,
        playlistOptions: {{
            autoPlay: false,
            // displayTime: 0,
            // addTime: 0,
            // removeTime: 0,
            // shuffleTime: 0
        }},
        swfPath: "/++plone++collective.playlist",
        solution: 'html, flash',
        supplied: "mp3, oga, ogg, wav",
        wmode: "window",
        useStateClassSkin: true,
        autoBlur: false,
        smoothPlayBar: true,
        keyEnabled: true,
        remainingDuration: true
    }});

}});"""
        return js.format(dtracks=json.dumps(self._dict_tracks()))

    def can_add_and_edit(self):
        try:
            # roles = api.user.get_roles()
            current = api.user.get_current()
            roles = current.getRoles()
        except api.user.UserNotFoundError:
            roles = []
        result = 'Manager' in roles or \
                 'Site Administrator' in roles or \
                 'Editor' in roles
        return result

    @ram.cache(lambda *args: time() // (60))  # one minute
    def getSiteLogo(self, site=None):
        if site is None:
            site = api.portal.get()
        site_url = site.absolute_url()
        if api.portal.get_registry_record('plone.site_logo', default=None):
            return '{}/@@site-logo'.format(site_url)  # flake8: noqa

    @ram.cache(lambda *args: time() // (60))  # one minute
    def css_collectiveplaylist(self):
        style = api.portal.get_registry_record('collective.playlist.style')
        return style

    @ram.cache(lambda *args: time() // (60))  # one minute
    def css_stylesheets_collectiveplaylist(self):
        stylesheets = api.portal.get_registry_record(
            'collective.playlist.stylesheets')
        result = u''
        tag = u'<link rel="stylesheet" type="text/css" href="{}" />'  # flake8: noqa
        for ss in stylesheets:
            result += tag.format(ss)
        return result

    @ram.cache(lambda *args: time() // 1)  # one second
    def copyright(self):
        context = self.context
        cr = context.copyright.output
        return cr
