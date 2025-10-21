# --- run_daily.ps1 ---
# Navigate to project directory
Set-Location "C:\development\Auto_job_applier_linkedIn"

# Activate the virtual environment
& "C:\development\Auto_job_applier_linkedIn\venv_win\Scripts\Activate.ps1"

# Run your Python script
python runAiBot.py

# log output for debugging
python runAiBot.py *> "C:\development\Auto_job_applier_linkedIn\logs\job_log.txt"
