# Analytics
Real time analytics of Arquivo.pt Data using Streamlit

## Setup

```bash
git clone https://github.com/arquivo/real-time-analytics.git
cd real-time-analytics
pip install --upgrade virtualenv
virtualenv -p python3 venv
source venv/bin/activate
pip install -r requirements.txt
```

## Run

```bash
streamlit run real_time_analytics.py -- --j (json file with google service) --k (Key Google Spreadsheet) --ws (Worksheet Google Spreadsheet)
```

## Docker

To test the Docker image, build and run it, execute:

```bash
docker compose build && docker compose up
```

## CI

This repository automatically pushes to the `arquivo` organization on DockerHub.
