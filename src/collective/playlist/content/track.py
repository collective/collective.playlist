# -*- coding: utf-8 -*-
from plone.app.textfield import RichText
from plone.autoform import directives
from plone.dexterity.content import Item
from plone.namedfile import field as namedfile
from plone.supermodel import model
from plone.supermodel.directives import fieldset
from z3c.form.browser.radio import RadioFieldWidget
from zope import schema
from zope.interface import implementer
from collective.playlist import _


class ITrack(model.Schema):
    """ Marker interfce and Dexterity Python Schema for Track
    """

    # TODO: validator: ALLOWED_AUDIOTYPES = ["mp3", "oga", "ogg", "wav"]
    audiofile = namedfile.NamedBlobFile (
        title=_(u'Audio'),
        description = _(u'mp3, oga, ogg, wav'),
        required=True,
    )
    


@implementer(ITrack)
class Track(Item):
    """
    """
