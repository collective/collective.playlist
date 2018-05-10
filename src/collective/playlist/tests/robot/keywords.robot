*** Settings *****************************************************************

Resource  plone/app/robotframework/annotate.robot
Resource  plone/app/robotframework/keywords.robot


*** Keywords *****************************************************************


Retract object
    Set Window Size  800  600
    Click Link  css=a.plone-toolbar-logo
    Click Element  plone-contentmenu-workflow
    Click Link  Retract

Select pop up window
    Select Window  NEW
    Log Location
    
Scroll Page
    Scroll Page To Location    0    2000

Scroll Page To Location
    [Arguments]    ${x_location}    ${y_location}
    Execute JavaScript    window.scrollTo(${x_location},${y_location})


# --- Given ------------------------------------------------------------------

a logged-in manager
  Enable autologin as  Manager
  
a logged-in site administrator
  Enable autologin as  Site Administrator  Contributor  Reviewer
  
Log in as site administrator
    Enable autologin as  Manager
    Create user  siteadmin  roles=('Contributor','Reviewer','Site Administrator')
    # Set autologin username  siteadmin
    Disable autologin
    Log in  siteadmin  siteadmin

an add playlist form
    Go To  ${PLONE_URL}/++add++playlist

a playlist 'My Playlist'
    Create content  type=playlist  id=my-playlist  title=My Playlist


an add track form in
    [Arguments]    ${parent_id}
    [Documentation]    Add track in current playlist
    Go To  ${PLONE_URL}/${parent_id}/++add++track

a track
    [arguments]  ${parent_id}  ${title}  ${filename}
    [documentation]  Adds a track to playlist with id "parent_id"

    Go To  ${PLONE_URL}/${parent_id}/edit
    Click Link  Settings
    Click Element  id=plone-contentmenu-factories
    Click Link  Track
    Input Text  name=form.widgets.IDublinCore.title  ${title}
    Choose File  name=form.widgets.audiofile  ${PATH_TO_TEST_FILES}/${filename}
    Click button  Save
    Page Should Contain  Item created


# --- WHEN -------------------------------------------------------------------

I type '${title}' into the title field
  Input Text  name=form.widgets.IDublinCore.title  ${title}

I submit the form
  Click Button  Save

I go to the playlist view
  Go To  ${PLONE_URL}/my-playlist
  # Wait until page contains  Site Map

I go to track ${track_id} in ${playlist_id}
    Go To  ${PLONE_URL}/${playlist_id}/${track_id}

# --- THEN -------------------------------------------------------------------

a playlist with the title '${title}' has been created
  # Wait until page contains  Site Map
  Page should contain  ${title}
  # Page should contain  Item created

I can see the playlist title '${title}'
  # Wait until page contains  Site Map
  Page should contain  ${title}


a track with the title '${title}' has been created
    Wait until page contains  Site Map
    Page should contain  ${title}
    Page should contain  Item created

I can see the track title '${title}'
    Wait until page contains  Site Map
    Page should contain  ${title}

