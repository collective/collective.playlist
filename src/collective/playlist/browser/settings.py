# coding: utf-8
from collective.playlist import _
from plone.app.registry.browser.controlpanel import ControlPanelFormWrapper
from plone.app.registry.browser.controlpanel import RegistryEditForm
from plone.z3cform import layout
from Products.Five.browser import BrowserView
from zope import schema
from zope.interface import Interface


class ISettings(Interface):
    """ Define settings data structure """

    style = schema.SourceText(
        title=_(u'Style'),
        description=_(u'Some style to be applied to playlist. CSS'),
        default=u'',
        required=False,
        )

    stylesheets = schema.List(
        title=_(u'Stylesheets'),
        description=_(
            u'Some stylesheets to be applied to playlist. e.g. https://fonts.googleapis.com/css?family=Ubuntu'), # noqa E501
        default=[],
        missing_value=None,
        required=False,
        value_type=schema.TextLine(),
        )


class SettingsEditForm(RegistryEditForm):
    """
    Define form logic
    """
    schema = ISettings
    schema_prefix = 'collective.playlist'
    label = u'Playlist settings'


class SettingsView(BrowserView):
    """
    View which wrap the settings form using ControlPanelFormWrapper to a
    HTML boilerplate frame.
    """

    def __call__(self):
        view_factor = layout.wrap_form(
            SettingsEditForm, ControlPanelFormWrapper)
        view = view_factor(self.context, self.request)
        return view()
