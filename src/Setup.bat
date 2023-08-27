@echo off

REM Check if Python is installed
python --version >nul 2>&1
if %errorlevel% NEQ 0 (
    set /p install_python=Python is not installed. Do you want to install it? (yes/no): 
    if /i "%install_python%"=="yes" (
        REM Download and install Python
        REM The following lines download the installer and execute it (for Windows only)
        curl -o python_installer.exe https://www.python.org/ftp/python/3.11.5/python-3.11.5-embed-amd64.zip
        python_installer.exe
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
