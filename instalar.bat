echo.
echo "Criando a pasta virtual...."
python.exe -m venv venv
echo.
echo "Acessando a pasta virtual do python..."
call venv\Scripts\activate.bat
echo on
echo.
echo "Atualizando o pip..."
python.exe -m pip install --upgrade pip
echo.
echo "Instalando o Django..."
pip install django
echo.
echo "Instalando flake8"
pip install -U flake8
echo.
echo "Instalando mypy"
pip install -U mypy
echo.
echo "Instalando autopep8"
pip install -U autopep8
echo.
@REM echo "Instalando Pillow"
@REM pip install -U pillow
@REM echo.
@REM echo "Instalado o Django-summernote"
@REM pip install -U django-summernote
@REM echo.
@REM echo "Instalando o MySQLClient"
@REM pip install -U mysqlclient

pause "Finalizado"