#!/bin/bash
echo "Akademize TDD project setup script"
echo "----------------------------------"

python --version
python -m pip --version

# Create and activate a virtual environment
python -m venv .venv
source .venv/bin/activate

# Install dependencies
python -m pip install -r requirements.txt
