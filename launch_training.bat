@echo off

:: Активация виртуального окружения
call venv\Scripts\activate

:menu
cls
echo Select "Emotion Analysis Training"[E] or "Sentiment Analysis Training"[S] or Quit[Q] to continue:
echo [E] - Run Emotion Analysis Training
echo [S] - Run Sentiment Analysis Training
echo [Q] - Quit

set /p choice=Enter your choice: 

if /i "%choice%"=="E" (
    python launch_train_emotion.py
) else if /i "%choice%"=="S" (
    python launch_train_sentiment.py
) else if /i "%choice%"=="Q" (
    exit
) else (
    echo Invalid choice. Please try again.
    pause
    goto menu
)

:: Деактивация виртуального окружения
deactivate