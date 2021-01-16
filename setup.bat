echo "Akademize TDD project setup script"
echo "----------------------------------"

python --version
python -m pip --version

REM Create and activate a virtual environment
call python -m venv .venv
call .venv\Scripts\activate

REM Install dependencies
call python -m pip install -r requirements.txt
