# ============================================================================
# DEXTERITY ROBOT TESTS
# ============================================================================
#
# Run this robot test stand-alone:
#
#  $ bin/test -s collective.playlist -t test_playlist.robot --all
#
# Run this robot test with robot server (which is faster):
#
# 1) Start robot server:
#
# $ bin/robot-server --reload-path src collective.playlist.testing.COLLECTIVE_PLAYLIST_ACCEPTANCE_TESTING
#
# 2) Run robot tests:
#
# $ bin/robot src/plonetraining/testing/tests/robot/test_playlist.robot
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

Library  Remote  ${PLONE_URL}/RobotRemote

Test Setup  Open test browser
Test Teardown  Close all browsers


*** Test Cases ***************************************************************

Scenario: As a site administrator I can add a playlist
    Given a logged-in site administrator
        and an add playlist form
    When I type 'My Playlist' into the title field
        and Scroll Page
        and I submit the form
    Then a playlist with the title 'My Playlist' has been created

Scenario: As a site administrator I can view a playlist
    Given a logged-in site administrator
        and a playlist 'My Playlist'
    When I go to the playlist view
    Then I can see the playlist title 'My Playlist'

