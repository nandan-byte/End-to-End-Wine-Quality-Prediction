FROM python:3.11-slim

WORKDIR /app

# Copy Python dependencies and source
COPY src /app
# Explicit source directory

RUN pip install -r requirements.txt

CMD ["python3", "app.py"]