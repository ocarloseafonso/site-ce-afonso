@echo off
echo Iniciando servidor local para teste do site Ateliê DK...
start "Servidor Atelie DK" python server.py
timeout /t 2 /nobreak >nul
start http://localhost:8080
exit
