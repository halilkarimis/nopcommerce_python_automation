pytest -s -v -m "sanity" --html=./Reports/report_chrome.html testCases/ --browser chrome
rem pytest -s -v -m "regression" --html=./Reports/report_chrome.html testCases/ --browser chrome

rem pytest -s -v -m "sanity" --html=./Reports/report_firefox.html testCases/ --browser firefox
rem pytest -s -v -m "regression" --html=./Reports/report_firefox.html testCases/ --browser firefox

rem pytest -s -v -m "sanity" --html=./Reports/report_ie.html testCases/ --browser ie
rem pytest -s -v -m "regression" --html=./Reports/report_ie.html testCases/ --browser ie

rem is for commenting
