@echo off

REM Set the path to the current directory
set CURRENT_DIR=%~dp0

REM Activate the virtual environment
call %CURRENT_DIR%env\Scripts\activate

REM Run the Python script
python %CURRENT_DIR%src\main.py --threshold 13000 --input "./demo/As Light Rain Falls Without Reason.txt" --output "output.csv" --sort_by "count"

echo Done!
pause

REM Deactivate the virtual environment
deactivate

