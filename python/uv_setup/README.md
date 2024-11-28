# Python project setup

install uv
install ruff (vs code extension)

## Initialize project

uv init --no-workspace

## Initialize virtual environment

python3 -m venv .venv
source .venv/bin/activate

## Make directories and files

mkdir .vscode
touch .vscode/settings.json
touch .vscode/extensions.json
touch .gitignore

mkdir src
mv hello.py src/main.py
touch src/__init__.py

mkdir tests
touch tests/tests_main.py

## Run and Test

python3 src/main.py
pytest tests/tests_main.py
