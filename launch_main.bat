@echo off

:: Активация виртуального окружения
call venv\Scripts\activate

:: Запуск Python-скрипта
python launch_app_ui.py

:: Деактивация виртуального окружения
deactivate
