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
