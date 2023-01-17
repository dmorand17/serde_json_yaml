# Should update this to use python:3 instead
FROM python:3.10-slim-buster

WORKDIR /app
# We copy just the requirements.txt first to leverage Docker cache
COPY requirements.txt .

RUN pip install -r requirements.txt
COPY serde_json_yaml.py .

# Set the command to run when the container starts
ENTRYPOINT ["python3", "serde_json_yaml.py"]
