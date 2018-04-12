.. This README is meant for consumption by humans and pypi. Pypi can render rst files so please do not use Sphinx features.
   If you want to learn more about writing documentation, please check out: http://docs.plone.org/about/documentation_styleguide.html
   This text does not appear on pypi or github. It is a comment.

===================
collective.playlist
===================

collective.playlist provides playlist and track content types and a pop up player.


.. figure:: playlist.png
    :width: 210px
    :align: center

    Playlist

Uses JPlayer_.


Documentation
-------------

Initial playlist
*******************

An initial playlist with tracks is created at /playlist.

Playlist
*********

A play button is shown if and only if a published playlist exists.

Click the play button to open the player. A qualified user is presented a menu to edit the playlist.


Customizations
--------------


Layout
***********

Layout can be modified in control panel.

Change Font
**************

.. figure:: font.png
    :width: 400px
    :align: center

    Use your own font

Background Image for your Playlist
************************************

Upload an image "background.jpg" to your Plone-Site.

Go to playlist control panel and add::

    html {
        background-image:url("background.jpg");
    }


Translations
------------

This product has been translated into

- german


Installation
------------

Install collective.playlist by adding it to your buildout::

    [buildout]

    ...

    eggs =
        collective.playlist


and then run ``bin/buildout``


Plone Version Compatibility
---------------------------

Works with Plone 5


Contribute
----------

- Issue Tracker: https://github.com/collective/collective.playlist/issues
- Source Code: https://github.com/collective/collective.playlist


License
-------

The project is licensed under the GPLv2.

Music:
© 2003 Miaow / Arnaud Laflaquiere - MiaowMusic.net

For JPLayer license see JPlayer_

Author
------

- Katja Süss, Rohberg ( @ksuess )

.. target-notes::

.. _JPlayer: http://jplayer.org/latest/demo-02-multi/
