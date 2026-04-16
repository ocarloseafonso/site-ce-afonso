@echo off
echo Iniciando servidor local para teste do site C.E. Afonso...
start "Servidor C.E. Afonso" python server.py
timeout /t 2 /nobreak >nul
start http://localhost:8080
exit
