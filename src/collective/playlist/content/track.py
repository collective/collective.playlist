# -*- coding: utf-8 -*-
from collective.playlist import _
from plone.dexterity.content import Item
from plone.namedfile import field as namedfile
from plone.supermodel import model
from zope.interface import implementer


class ITrack(model.Schema):
    """ Marker interfce and Dexterity Python Schema for Track
    """

    audiofile = namedfile.NamedBlobFile(
        title=_(u'Audio'),
        description=_(u'mp3, oga, ogg, wav'),
        required=True,
    )


@implementer(ITrack)
class Track(Item):
    """
    """
