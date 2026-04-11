@echo off
setlocal
title Atualizador de Site - C.E. Afonso Soluções Digitais
cls
echo ======================================================
echo    ENVIANDO ALTERACOES PARA O GITHUB + VERCEL
echo ======================================================
echo.

:: Verifica se há mudanças
git status --short | findstr /R "^" >nul
if errorlevel 1 (
    echo [AVISO] Nenhuma alteracao encontrada para subir.
    echo.
    pause
    exit /b
)

:: Seleciona todas as mudanças
echo [+] Preparando arquivos...
git add .

:: Pergunta a mensagem de commit
echo [+] O que voce mudou no site?
set /p msg="Descricao (ou Enter para padrao): "
if "%msg%"=="" set msg="Atualizacao via icone automatizado"

:: Commit e Push
echo.
echo [+] Criando versao: %msg%
git commit -m "%msg%"

echo.
echo [+] Enviando para o GitHub...
git push origin main

if errorlevel 1 (
    echo.
    echo [ERRO] Falha ao enviar para o GitHub. Verifique sua internet.
) else (
    echo.
    echo ======================================================
    echo   SUCESSO! O Vercel iniciara a atualizacao em breve.
    echo ======================================================
)

echo.
pause
exit /b
