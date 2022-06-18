# coding: utf-8
from collective.playlist import _
from plone.app.registry.browser import controlpanel
from zope import schema
from zope.interface import Interface


class ISettings(Interface):
    """Define settings data structure"""

    style = schema.SourceText(
        title=_("Style"),
        description=_("Some style to be applied to playlist. CSS"),
        default="",
        required=False,
    )

    stylesheets = schema.List(
        title=_("Stylesheets"),
        description=_(
            "Some stylesheets to be applied to playlist. e.g. https://fonts.googleapis.com/css?family=Ubuntu"
        ),  # noqa E501
        default=[],
        missing_value=None,
        required=False,
        value_type=schema.TextLine(),
    )


class SettingsEditForm(controlpanel.RegistryEditForm):
    """
    Define form logic
    """

    schema = ISettings
    schema_prefix = "collective.playlist"
    label = "Playlist settings"


class SettingsView(controlpanel.ControlPanelFormWrapper):
    """Control panel form wrapper."""

    form = SettingsEditForm
