@echo off
REM Launch Beburos from venv

echo Activating virtual environment...
call venv311\Scripts\activate.bat

echo Running Beburos app...
python main.py --mode app

pause
