@echo off
:: Check for Python Installation
python --version 3>NUL
if errorlevel 1 goto errorNoPython

:: Reaching here means Python is installed.
:: Execute stuff...

pip install pyfiglet colorama pillow survey
echo "python bin/main.py" > main.bat
echo "Sucessfully built Pyndows, to launch it, type in terminal: 'start main.bat'."

:: Once done, exit the batch file -- skips executing the errorNoPython section
goto:eof
del build.bat

:errorNoPython
echo.
echo "Error! Python is not installed."