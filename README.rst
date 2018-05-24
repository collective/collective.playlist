***************************
Player for Audio Playlist
***************************

.. contents:: Table of Contents

Summary
============
 
The Plone add-on collective.playlist provides a playlist and a track content type. The player is per default a sticky footer. Optional as an alternative is a player in a pop up window that can be launched via a play button.


Sticky Footer
=============

The site is navigable while the player continues to play.

.. figure:: https://raw.githubusercontent.com/collective/collective.playlist/master/stickyplayer.png
    :width: 500px
    :align: center
    :alt: Sticky Footer Player

    Sticky Footer Player

.. figure:: https://raw.githubusercontent.com/collective/collective.playlist/master/stickyplayer_mobile.png
    :width: 210px
    :align: center
    :alt: Sticky Footer Player Mobile

    Sticky Footer Player on Mobile Device
    

Pop Up Player
=============

A click on the play button opens a window with playlist and player.

.. figure:: https://raw.githubusercontent.com/collective/collective.playlist/master/playlist.png
    :width: 500px
    :align: center
    :alt: Playlist

    Playlist


.. figure:: https://raw.githubusercontent.com/collective/collective.playlist/master/playlist_mobile.png
    :width: 210px
    :align: center
    :alt: Playlist Mobile evices

    Playlist on Mobile Device



Documentation
=============

The Add-On uses JPlayer [#f1]_.

Initial playlist
----------------

An initial playlist with tracks is created at /playlist.

Sticky Footer
-------------

The site is navigable while the player continues to play thanks to pjax [#f2]_. Pjax works with browsers that support the history.pushState() API. When the API isn't supported, Pjax goes into fallback mode (and it just does nothing). See Browser Support [#f3]_.

The sticky footer is shown if and only if a published playlist exists. For a qualified user it's shown anyway.

Pop Up Player
-------------

The pop up player is per default deactivated. You can activate it via @@manage-viewlets view like
localhost:8080/Plone/@@manage-viewlets

A play button is shown on top of each page if and only if a published playlist exists. For a qualified user it's shown anyway.

Click the play button to open the player. A menu to edit the playlist and its tracks is presented to qualified users.


Customizations
===============

Layout
------

Layout can be modified in control panel.

Change Font
-------------

.. figure:: https://raw.githubusercontent.com/collective/collective.playlist/master/font.png
    :width: 300px
    :align: center
    :alt: How to use your font

    Use your font

Background Image for your Pop Up Playlist
------------------------------------------

Upload an image "background.jpg" to your Plone-Site.

Go to playlist control panel and add::

    html {
        background-image:url("background.jpg");
    }


Translations
==============

This product has been translated into

- german


Installation
==============

Install collective.playlist by adding it to your buildout.


Plone Version Compatibility
============================

Plone 5

.. image:: https://travis-ci.org/collective/collective.playlist.svg?branch=master&t=1002
    :target: https://travis-ci.org/collective/collective.playlist
    
.. image:: https://coveralls.io/repos/github/collective/collective.playlist/badge.svg?branch=master&t=1002
    :target: https://coveralls.io/github/collective/collective.playlist?branch=master


Contribute
============

- Issue Tracker: https://github.com/collective/collective.playlist/issues
- Source Code: https://github.com/collective/collective.playlist



License
========

The project is licensed under the GPLv2.

Music:
© 2003 Miaow / Arnaud Laflaquiere - MiaowMusic.net

For JPLayer license see JPlayer [#f1]_


Credits
=========

Developed with the support of:

.. image:: https://raw.githubusercontent.com/collective/collective.playlist/master/zhref.png
    :width: 220px
    :align: left
    :alt: Reformierte Kirche Kanton Zürich
    :target: http://www.zhref.ch


Author
========

- Katja Süss, Rohberg ( @ksuess )


Footnotes
============

.. target-notes::

.. [#f1] `JPlayer <http://jplayer.org/latest/demo-02-multi/>`_ : Open Source media library written in JavaScript.
.. [#f2] `pjax <https://github.com/MoOx/pjax>`_ : Enable fast Ajax navigation on any website (using pushState + xhr)  
.. [#f3] Browser Support `Caniuse <https://caniuse.com/#search=pushstate>`_
