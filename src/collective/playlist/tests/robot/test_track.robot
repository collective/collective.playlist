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

Resource  plone/app/robotframework/selenium.robot
Resource  plone/app/robotframework/keywords.robot

Library  Remote  ${PLONE_URL}/RobotRemote

Test Setup  Open test browser
Test Teardown  Close all browsers


*** Test Cases ***************************************************************

Scenario: As a site administrator I can add a track
  Given a logged-in site administrator
    and an add track form
   When I type 'My Track' into the title field
    and I submit the form
   Then a track with the title 'My Track' has been created

Scenario: As a site administrator I can view a track
  Given a logged-in site administrator
    and a track 'My Track'
   When I go to the track view
   Then I can see the track title 'My Track'


*** Keywords *****************************************************************

# --- Given ------------------------------------------------------------------

a logged-in site administrator
  Enable autologin as  Site Administrator

an add track form
  Go To  ${PLONE_URL}/++add++track

a track 'My Track'
  Create content  type=track  id=my-track  title=My Track


# --- WHEN -------------------------------------------------------------------

I type '${title}' into the title field
  Input Text  name=form.widgets.IDublinCore.title  ${title}

I submit the form
  Click Button  Save

I go to the track view
  Go To  ${PLONE_URL}/my-track
  Wait until page contains  Site Map


# --- THEN -------------------------------------------------------------------

a track with the title '${title}' has been created
  Wait until page contains  Site Map
  Page should contain  ${title}
  Page should contain  Item created

I can see the track title '${title}'
  Wait until page contains  Site Map
  Page should contain  ${title}
