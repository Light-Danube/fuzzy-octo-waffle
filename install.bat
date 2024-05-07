@echo off
echo Creating virtual environment...
python -m venv venv
echo Virtual environment created.

echo Activating virtual environment...
call venv\Scripts\activate
echo Virtual environment activated.

echo Installing requirements...
pip install -r requirements.txt
echo Requirements installed.

echo Installation complete.

echo Deactivating virtual environment...
deactivate
echo Virtual environment deactivated.

pause

