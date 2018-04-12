***setting***
Library         Selenium2Library

***Test case***
Open Google
        Open Google

*** Variables ***
#01Welcome Page
${URLwelcome}           https://www.google.com
# ${BROWSER}              chrome
${BROWSER}              firefox

***Keyword***
Open Google
        Open Browser            ${URLwelcome}    ${BROWSER}