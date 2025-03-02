# Reddit cli test example

## Installation

**Install `uv`:** 
[Installation Instructions.](https://docs.astral.sh/uv/getting-started/installation/)

**Clone the repository and navigate to directory:**
```bash
git clone https://github.com/todx0/reddit-cli-example.git && cd reddit-cli-example
```

**Create `.env` and edit secrets:**
```bash
cp .env.example .env
```

**Create and activate a virtual environment:**
```bash
uv venv .venv
source .venv/bin/activate
```

**Install dependencies:**
```bash
uv pip install -r pyproject.toml
```

## Usage

### Run command
```bash
### will fetch 5 latest post from a subreddit
python src/main.py https://www.reddit.com/r/xbiking/ fetch_latest_posts 5
```

### Run tests
```bash
python -m pytest -v
```