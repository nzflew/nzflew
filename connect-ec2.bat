@echo off
set HOST=54.252.99.211
set USER=ubuntu
set KEY="C:\Users\nzfle\Dropbox\Escene\ec2\keys\gsg-keypair-aus_sydney.pem"

echo Connecting to %USER%@%HOST% using key %KEY%...
ssh -i %KEY% %USER%@%HOST%

echo.
echo Connection closed. Press any key to exit.
pause >nul
