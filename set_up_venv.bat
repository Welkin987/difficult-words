@echo off

REM Set the path to the current directory
set CURRENT_DIR=%~dp0

REM Create a Python virtual environment
python -m venv %CURRENT_DIR%env

REM Activate the virtual environment
call %CURRENT_DIR%env\Scripts\activate

REM Upgrade pip to avoid potential issues
python -m pip install --upgrade pip

REM Install nltk version 3.8.1
pip install nltk==3.8.1

echo Virtual environment created and nltk 3.8.1 installed.
echo To activate the environment, run: run_in_venv.bat

pause