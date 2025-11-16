@echo off
REM ============================================
REM DoceLang - Script de Build e Testes
REM ============================================

echo.
echo ====================================
echo DOCELANG - COMPILADOR
echo Projeto Compiladores 2025
echo ====================================
echo.

REM Verificar se Python está instalado
python --version >nul 2>&1
if errorlevel 1 (
    echo [ERRO] Python nao encontrado!
    echo Por favor, instale Python 3.7 ou superior.
    pause
    exit /b 1
)

echo [OK] Python instalado

REM Menu de opções
:menu
echo.
echo Escolha uma opcao:
echo.
echo 1 - Executar testes do lexer
echo 2 - Processar todos os exemplos .doce
echo 3 - Processar arquivo especifico
echo 4 - Verificar estrutura do projeto
echo 5 - Limpar arquivos temporarios
echo 0 - Sair
echo.
set /p opcao="Digite a opcao: "

if "%opcao%"=="1" goto testes
if "%opcao%"=="2" goto exemplos
if "%opcao%"=="3" goto arquivo
if "%opcao%"=="4" goto estrutura
if "%opcao%"=="5" goto limpar
if "%opcao%"=="0" goto fim
goto menu

:testes
echo.
echo ====================================
echo EXECUTANDO TESTES DO LEXER
echo ====================================
echo.
python lexer\test_lexer.py
pause
goto menu

:exemplos
echo.
echo ====================================
echo PROCESSANDO EXEMPLOS .doce
echo ====================================
echo.
python run_examples.py
pause
goto menu

:arquivo
echo.
set /p arquivo="Digite o caminho do arquivo .doce: "
echo.
echo ====================================
echo PROCESSANDO: %arquivo%
echo ====================================
echo.
python -c "from lexer.lexer import DoceLangLexer; from lexer.tokens import print_tokens_table; code=open('%arquivo%', 'r', encoding='utf-8').read(); tokens=DoceLangLexer(code).tokenize(); print(f'Tokens: {len(tokens)}'); print_tokens_table(tokens)"
pause
goto menu

:estrutura
echo.
echo ====================================
echo ESTRUTURA DO PROJETO
echo ====================================
echo.
tree /F /A
pause
goto menu

:limpar
echo.
echo ====================================
echo LIMPANDO ARQUIVOS TEMPORARIOS
echo ====================================
echo.
del /s /q *.pyc 2>nul
del /s /q __pycache__ 2>nul
echo [OK] Limpeza concluida
pause
goto menu

:fim
echo.
echo ====================================
echo Ate logo!
echo ====================================
echo.
exit /b 0
