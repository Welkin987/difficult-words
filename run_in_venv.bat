@echo off

REM Set the path to the current directory
set CURRENT_DIR=%~dp0

REM Activate the virtual environment
call %CURRENT_DIR%env\Scripts\activate

REM Run the Python script
python %CURRENT_DIR%src\main.py --threshold 10000 --input "./demo/the_little_prince.txt" --output "output.csv" --sort_by "rank"

echo Done!
pause

REM Deactivate the virtual environment
deactivate

