# Reddit cli test example

## Installation

**Install `uv`:**
```bash
curl -LsSf [https://install.astral.sh](https://install.astral.sh) | sh
# Or if you have homebrew
brew install astral-sh/tap/uv
```

**Clone the repository and navigate to directory**
```bash
git clone && cd
```

**Create `.env` and edit secrets**
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