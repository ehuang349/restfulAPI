@echo off
REM Set environment variables from the .env file
for /f "tokens=1,2 delims==" %%a in (environments/prod.env) do set %%a=%%b

REM Start the FastAPI application
python main.py