rem imp points
rem to comment out all the commands which you don't wan't to use ; use rem infront of command
rem always use "" to write marker name like "sanity"
rem can run more than one command which will execute one after another
rem use diff report for diff browsers

rempytest -v -s -m "sanity" --html=./Reports/report.html testCases/ --browser chrome
rem pytest -v -s -m "regression" --html=./Reports/report.html testCases/ --browser chrome
rem pytest -v -s -m "sanity and regression" --html=./Reports/report.html testCases/ --browser chrome
pytest -v -s -m "sanity or regression" --html=./Reports/report.html testCases/ --browser chrome

rempytest -v -s -m "sanity" --html=./Reports/report.html testCases/ --browser firefox
rem pytest -v -s -m "regression" --html=./Reports/report.html testCases/ --browser firefox
rem pytest -v -s -m "sanity and regression" --html=./Reports/report.html testCases/ --browser firefox
pytest -v -s -m "sanity or regression" --html=./Reports/report.html testCases/ --browser firefox


cmd /k
rem to stop cmd from closing immediately after process ends