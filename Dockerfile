# Use official Python image as base
FROM python:3.9-slim

# Set environment variable for Google Service Account JSON
ENV GOOGLE_SERVICE_ACCOUNT_JSON=/run/secrets/google_service_account.json

ARG KEY1

ARG KEY2

# The port where the Streamlit app will run
ENV SERVER_PORT=8501

# The base URL path where the app will be served (e.g., "myapp" for "/myapp")
# Leave empty for root ("/")
ENV BASE_URL_PATH="/"

# Set working directory
WORKDIR /app

# Copy requirements.txt
COPY requirements.txt .
# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY real_time_analytics.py .

# Expose Streamlit default port
EXPOSE $SERVER_PORT

# Set environment variables (optional, for Streamlit)
ENV PYTHONUNBUFFERED=1

HEALTHCHECK CMD curl --fail http://localhost:$SERVER_PORT/_stcore/health

# Startup command (expects arguments to be provided at runtime)
ENTRYPOINT streamlit run real_time_analytics.py --browser.serverAddress=0.0.0.0 --browser.serverPort=${SERVER_PORT} --theme.base='dark' --browser.gatherUsageStats=false -- --pathjson ${GOOGLE_SERVICE_ACCOUNT_JSON} --key1 "${KEY1}" --key2 "${KEY2}"
