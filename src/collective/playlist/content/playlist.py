# -*- coding: utf-8 -*-
from collective.playlist import _
from plone.app.textfield import RichText
from plone.dexterity.content import Container
from plone.supermodel import model
from zope.interface import implementer


class IPlaylist(model.Schema):
    """ Marker interfce and Dexterity Python Schema for Playlist
    """

    copyright = RichText(title=_(u'Copyright'),
                         default=u'',
                         required=False)


@implementer(IPlaylist)
class Playlist(Container):
    """
    """
