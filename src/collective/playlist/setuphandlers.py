# coding: utf-8
from plone import api
from Products.CMFPlone.interfaces import INonInstallable
from zope.interface import implementer

import os


@implementer(INonInstallable)
class HiddenProfiles(object):  # pragma: no cover

    def getNonInstallableProfiles(self):
        """Hide uninstall profile from site-creation and quickinstaller."""
        return [
            'collective.playlist:uninstall',
        ]


def post_install(context):
    """Post install script"""
    # Do something at the end of the installation of this package.
    portal = api.portal.get()
    _create_content(portal)
    _deactivate_popup(portal)


def uninstall(context):
    """Uninstall script

    delete playlists with tracks"""

    playlists = api.content.find(portal_type='playlist')
    playlists = [b.getObject() for b in playlists]
    api.content.delete(objects=playlists)


def _create_content(portal):
    playlistid = 'playlist'
    if not portal.get(playlistid, False):
        playlist = api.content.create(
            type='playlist',
            container=portal,
            title=u'Playlist',
            id=playlistid,
        )
        for track_number in range(1, 4):
            track_id = u'track-{0}'.format(str(track_number))
            track_name = u'Track {0}'.format(str(track_number))
            track = api.content.create(
                type='track',
                container=playlist,
                title=track_name,
                id=track_id,
            )
            track.audiofile = _load_file(track_number)
            api.content.transition(obj=track, to_state='published')

        # NOTE: if your plone site is not a vanilla plone
        # you can have different workflows on folders and files
        # or different transitions names so this could fail
        # and you'll need to publish the tracks as well
        # or do that manually TTW.
        api.content.transition(obj=playlist, to_state='published')


def _load_file(track_number):
    from plone.namedfile.file import NamedBlobFile
    filename = os.path.join(
        os.path.dirname(__file__),
        'resources',
        'tracks',
        'track-{0}.mp3'.format(track_number),
    )
    return NamedBlobFile(
        data=open(filename, 'r').read(),
        filename=u'track-{0}.mp3'.format(track_number),
    )


def _deactivate_popup(portal):
    view = portal.restrictedTraverse('@@manage-viewlets')
    view.hide('plone.portalheader', 'collective.playlist.playerbuttonviewlet')
