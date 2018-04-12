# ============================================================================
# DEXTERITY ROBOT TESTS
# ============================================================================
#
# Run this robot test stand-alone:
#
#  $ bin/test -s collective.playlist -t test_track.robot --all
#
# Run this robot test with robot server (which is faster):
#
# 1) Start robot server:
#
# $ bin/robot-server --reload-path src collective.playlist.testing.COLLECTIVE_PLAYLIST_ACCEPTANCE_TESTING
#
# 2) Run robot tests:
#
# $ bin/robot src/plonetraining/testing/tests/robot/test_track.robot
#
# See the http://docs.plone.org for further details (search for robot
# framework).
#
# ============================================================================

*** Settings *****************************************************************

Variables  collective/playlist/tests/variables.py

Resource  plone/app/robotframework/selenium.robot
Resource  plone/app/robotframework/annotate.robot
Resource  plone/app/robotframework/keywords.robot
Resource  keywords.robot

Library   Remote  ${PLONE_URL}/RobotRemote

Test Setup  Open test browser
Test Teardown  Close all browsers


*** Test Cases ***************************************************************

Scenario: As a site administrator I can add a track
    Given a logged-in site administrator
        and a playlist 'My Playlist'
        and an add track form in  my-playlist
    When I type 'My Track' into the title field
        and Choose File  name=form.widgets.audiofile  ${PATH_TO_TEST_FILES}/track-1.mp3
        and I submit the form
    Then a track with the title 'My Track' has been created

Scenario: As a Site Administrator I can view a track
    Given a logged-in site administrator
        and a playlist 'My Playlist'
        and a track  my-playlist  My Track  track-1.mp3
    When I go to track my-track in my-playlist
    Then I can see the track title 'My Track'
