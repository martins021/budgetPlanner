# Project Setup

```sh
# Install Poetry
curl -sSL https://install.python-poetry.org | python3 -

# Add Poetry to PATH
nano ~/.bashrc
export PATH="/home/user/.local/bin:$PATH"
source ~/.bashrc
poetry --version

# Setup the Project
poetry self add poetry-plugin-shell
poetry shell
poetry install

# Run
poetry run python manage.py runserver

# default theme:
https://coolors.co/04773b-9a8f97-c3baba-e9e3e6-b2b2b2
