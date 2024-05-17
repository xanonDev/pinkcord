@echo off 
set /p install=Do you want to start the Pinkcord 2.0 installation? (yes/no): 

if /i "%install%"=="yes" (
    python Setup.py || (
        py Setup.py
    )
) else (
    echo Installation canceled.
)

pause
