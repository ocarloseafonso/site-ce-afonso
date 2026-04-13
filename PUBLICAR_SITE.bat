@echo off
title Publicador C.E. Afonso
echo.
echo  ========================================
echo    ENVIANDO ATUALIZACOES PARA O AR...
echo  ========================================
echo.

:: Garantir que estamos na pasta certa
cd /d "%~dp0"

:: 1. Salvar as mudancas
echo  [1/3] Preparando arquivos...
git add -A

:: 2. Criar a versao
echo  [2/3] Criando versao...
git commit -m "Atualizacao automatica: %date% %time%"

:: 3. Enviar
echo  [3/3] Enviando para o servidor...
git push origin main

echo.
echo  ========================================
echo    SUCESSO! Site atualizado.
echo  ========================================
echo.
echo  Acesse: https://ceafonso.com.br
echo  (Pode levar 1 minuto para mudar no ar)
echo.
pause
