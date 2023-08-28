@echo off

REM Check if Python is installed
python --version >nul 2>&1
if %errorlevel% NEQ 0 (
    set /p install_python=Python is not installed. Do you want to install it? (yes/no): 
    if /i "%install_python%"=="yes" (
        REM Download and install Python
        REM The following lines download the installer and execute it (for Windows only)
        bitsadmin /transfer "PythonInstaller" https://www.python.org/ftp/python/3.11.5/python-3.11.5-embed-amd64.zip %CD%\python_installer.zip
        tar -xf python_installer.zip
        cd Python-3.11.5-embed-amd64
        python_installer.exe
        cd ..
        REM Add code here to install Python on other platforms
    ) else (
        echo Python installation canceled.
        pause
        exit
    )
)

set /p install=Do you want to start the Pinkcord installation? (yes/no): 

if /i "%install%"=="yes" (
    python Setup.py
    py Setup.py
) else (
    echo Installation canceled.
)

pause
