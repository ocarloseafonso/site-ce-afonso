@echo off
setlocal
echo ====================================================
echo    Ferramenta de Sincronização - Ateliê DK
echo ====================================================
echo.
echo Verificando Node.js...
node -v >nul 2>&1
if %errorlevel% neq 0 (
    echo [ERRO] Node.js não encontrado. Por favor, instale o Node.js.
    pause
    exit /b
)

echo Atualizando referências de imagens...
node scripts/sync_images.js

echo.
echo ====================================================
echo    Processo Concluído! O site agora reflete suas
echo    mudanças nas pastas de imagens.
echo ====================================================
echo.
pause
