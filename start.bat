@echo off
title Plant Disease Detector
echo ========================================
echo    PLANT DISEASE DETECTOR
echo ========================================
echo.
echo Starting Dashboard...
start "" "dashboard/index.html"
echo.
echo Starting Web App...
cd webapp
start streamlit run app.py --server.port 8501
echo.
echo ========================================
echo    App running at: http://localhost:8501
echo    Dashboard opened in browser
echo ========================================
echo.
pause