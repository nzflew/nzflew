@echo off
set HOST=media-server
set USER=mark

echo Connecting to %USER%@%HOST%...
ssh %USER%@%HOST%

echo.
echo Connection closed. Press any key to exit.
pause >nul
