@echo off
setlocal EnableDelayedExpansion
title Publicar Site - C.E. Afonso Solucoes Digitais
cls
echo.
echo  =====================================================
echo    PUBLICAR SITE - C.E. Afonso Solucoes Digitais
echo  =====================================================
echo.

:: --- PASSO 1: Verificar se estamos no repositorio correto ---
git rev-parse --is-inside-work-tree >nul 2>&1
if errorlevel 1 (
    echo  [ERRO] Esta pasta nao e um repositorio Git valido.
    echo  Verifique se voce esta na pasta correta do site.
    echo.
    pause
    exit /b 1
)

:: --- PASSO 2: Mostrar status atual ---
echo  [INFO] Verificando alteracoes no site...
echo.
git status --short
echo.

:: --- PASSO 3: Adicionar TODAS as alteracoes (novas, modificadas e deletadas) ---
git add -A

:: --- PASSO 4: Verificar se ha algo para commitar ---
git diff --cached --quiet
if errorlevel 1 (
    goto :tem_alteracoes
) else (
    echo  [AVISO] Nenhuma alteracao detectada para publicar.
    echo.
    echo  O site ja esta atualizado no GitHub e Vercel.
    echo.
    pause
    exit /b 0
)

:tem_alteracoes
:: --- PASSO 5: Exibir o que sera enviado ---
echo  [+] Os seguintes arquivos serao publicados:
git diff --cached --name-only
echo.

:: --- PASSO 6: Solicitar descricao (com valor padrao seguro) ---
echo  [+] Descreva o que voce alterou no site:
echo      (Pressione Enter para usar a descricao padrao)
echo.
set "msg="
set /p "msg=  Descricao: "

if "!msg!"=="" (
    set "msg=Atualizacao do site"
)

:: --- PASSO 7: Criar versao (commit) ---
echo.
echo  [+] Criando versao: !msg!
git commit -m "!msg!"

if errorlevel 1 (
    echo.
    echo  [ERRO] Falha ao criar a versao. Verifique as mensagens acima.
    echo.
    pause
    exit /b 1
)

:: --- PASSO 8: Enviar para GitHub ---
echo.
echo  [+] Enviando para o GitHub...
git push origin main

if errorlevel 1 (
    echo.
    echo  =====================================================
    echo   [ERRO] Falha ao enviar para o GitHub!
    echo  =====================================================
    echo.
    echo  Possiveis causas:
    echo   - Sem conexao com a internet
    echo   - Credenciais do GitHub expiradas
    echo   - Conflito com versao remota (tente: git pull)
    echo.
    pause
    exit /b 1
)

:: --- PASSO 9: Sucesso! ---
echo.
echo  =====================================================
echo   SUCESSO! Site publicado com sucesso!
echo  =====================================================
echo.
echo  O que foi feito:
echo   [OK] Arquivos verificados e preparados
echo   [OK] Versao criada: !msg!
echo   [OK] Enviado para o GitHub
echo   [OK] Vercel iniciara a atualizacao automaticamente
echo.
echo  Acesse: https://ceafonso.com.br
echo  (A atualizacao pode levar de 30 a 90 segundos)
echo.
pause
exit /b 0
