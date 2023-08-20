set /p install=Do you want to start the Pinkcord installation? (yes/no): 

if /i "%install%"=="yes" (
    python setup.py
    py setup.py
) else (
    echo Installation canceled.
)

pause
