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

Scenario: Play button is shown
    Go to homepage
    a play button is visible

Scenario: Play button is shown if and only if a published playlist exists
    Enable autologin as  Site Administrator
    Go to homepage
    a play button is visible
    Click play button
    Select pop up window
    a playlist is visible

    Click Link  edit playlist
    Retract object
    Disable autologin
    Log out
    a play button is not visible
    

*** Keywords *****************************************************************

Click play button
    Click Link  css=a.playlist-button

# Wait until playlist is open
#     Wait Until Page Contains Element  css=#jp_container_playlist


# --- THEN -------------------------------------------------------------------

a play button is visible
    Page should contain element  css=a.playlist-button
    
a play button is not visible
    Page should not contain element  css=a.playlist-button
    
a playlist is visible
    Page should contain element  css=#jp_container_playlist