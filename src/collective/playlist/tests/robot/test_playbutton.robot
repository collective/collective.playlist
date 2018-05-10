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

# Initial content: published playlist with three tracks

Scenario: Play button is shown if and only if a published playlist exists
    # Log in as site administrator
    Given a logged-in site administrator
    Go to homepage
    a play button is not visible
    
    Given a logged-in manager
    Go To  ${PLONE_URL}/@@manage-viewlets
    # make playbutton visible:
    Go To  ${PLONE_URL}/@@manage-viewlets?show=plone.portalheader%3Acollective.playlist.playerbuttonviewlet
    Click Button  name=form.button.confirm
    
    Given a logged-in site administrator
    Go to homepage
    a play button is visible
    Click play button
    Select pop up window
    Wait until Page contains  edit playlist

    Click Link  edit playlist
    Retract object
    Disable autologin
    Log out
    Wait until logged out
    a play button is not visible


*** Keywords *****************************************************************

Click play button
    Click Link  css=a.playlist-button

Wait until playlist is open
    Wait Until Page Contains  Track 1

Wait until logged out
    Wait Until Page Contains  You are now logged out


# --- THEN -------------------------------------------------------------------

a play button is visible
    Page should contain element  css=a.playlist-button

a play button is not visible
    Page should not contain element  css=a.playlist-button

a playlist is visible
    Page should contain element  css=#jp_container_playlist