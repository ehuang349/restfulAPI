@echo off
REM Set environment variables from the .env file
for /f "tokens=1,2 delims==" %%a in (environments/prod.env) do set %%a=%%b

REM Kill the existing Uvicorn process
for /f "tokens=5" %%a in ('netstat -ano ^| findstr :8000') do taskkill /f /pid %%a


REM Start the FastAPI application
python main.py