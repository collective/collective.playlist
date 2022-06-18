# coding: utf-8

from collective.playlist import ALLOWED_AUDIOTYPES
from plone import api
from plone.dexterity.browser.view import DefaultView
from plone.memoize import ram
from Products.CMFPlone.resources import add_bundle_on_request
from Products.CMFPlone.resources import add_resource_on_request
from Products.CMFPlone.resources import remove_bundle_on_request
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from time import time

import json
import logging


logger = logging.getLogger(__name__)


class PlaylistBaseView(DefaultView):
    """Base View"""

    def getTracks(self):
        """list of track dictionaries

        [{u'mp3':
                u"http://nohost/plone/playlist/track-1/@@download/audiofile/track-1.mp3",
            "title": "Track 1"},
        {u'mp3':
                u"http://nohost/plone/playlist/track-2/@@download/audiofile/track-2.mp3",
            "title": "Track 2"},
        {u'mp3':
                u"http://nohost/plone/playlist/track-3/@@download/audiofile/track-3.mp3",
            "title": "Track 3"}]"""

        context = self.context
        items = context.contentItems()
        tracks = [
            item
            for item in items
            if (
                item[1].portal_type in ["track", "Link"]
                and api.content.get_state(obj=item[1]) == "published"
            )
        ]
        tracklist = []
        for tr in tracks:
            title = tr[1].title
            if tr[1].portal_type == "track":
                filename = tr[1].audiofile.filename
                address = "/".join(
                    [context.absolute_url(), tr[0], "@@download/audiofile", filename]
                )
                format = filename.split(".")[-1]
                format = format in ALLOWED_AUDIOTYPES and format or "mp3"
            elif tr[1].portal_type == "Link":
                remoteUrl = tr[1].remoteUrl
                if remoteUrl.startswith("${portal_url}"):
                    obj = api.content.get(UID=remoteUrl.split("/")[-1])
                    try:
                        filename = obj.file.filename
                    except Exception as e:
                        logger.error(
                            "*** getTracks. Link auf non audio file. ({})".format(e)
                        )
                        continue
                    address = "/".join(
                        [obj.absolute_url(), "@@download/file", filename]
                    )
                    format = filename.split(".")[-1]
                    format = format in ALLOWED_AUDIOTYPES and format or "mp3"
                else:
                    address = remoteUrl
                format = address.split(".")[-1]
                format = format in ALLOWED_AUDIOTYPES and format or "mp3"
            else:
                continue
            tracklist.append({"title": title, format: address})
        logger.info("tracklist {}".format(tracklist))
        return tracklist

    def getJSONTracks(self):
        """list of json track dictionaries"""
        return json.dumps(self.getTracks())

    def can_add_and_edit(self):
        # todo: remove after fix of robottests bug
        try:
            # roles = api.user.get_roles()
            current = api.user.get_current()
            roles = current.getRoles()
        except api.user.UserNotFoundError:  # pragma: no cover
            roles = []
        result = (
            "Manager" in roles or "Site Administrator" in roles or "Editor" in roles
        )
        return result

    @ram.cache(lambda *args: time() // (60))  # one minute
    def getSiteLogo(self, site=None):
        if site is None:
            site = api.portal.get()
        site_url = site.absolute_url()
        if api.portal.get_registry_record("plone.site_logo", default=None):
            return "{}/@@site-logo".format(site_url)  # flake8: noqa

    @ram.cache(lambda *args: time() // (60))  # one minute
    def css_collectiveplaylist(self):
        style = api.portal.get_registry_record("collective.playlist.style")
        return style

    @ram.cache(lambda *args: time() // (60))  # one minute
    def css_stylesheets_collectiveplaylist(self):
        stylesheets = (
            api.portal.get_registry_record("collective.playlist.stylesheets") or []
        )
        result = ""
        tag = '<link rel="stylesheet" type="text/css" href="{}" />'  # flake8: noqa
        for ss in stylesheets:
            result += tag.format(ss)
        return result

    def copyright(self):
        context = self.context
        cr = context.copyright.output
        return cr


class PlaylistPopupView(PlaylistBaseView):
    """ """

    template = ViewPageTemplateFile("templates/playlistpopupview.pt")

    def __call__(self):
        return self.template()


class PlaylistFooterView(PlaylistBaseView):
    """ """

    template = ViewPageTemplateFile("templates/playlistfooterview.pt")

    def __call__(self):
        return self.template()
