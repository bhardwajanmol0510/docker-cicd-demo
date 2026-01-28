FROM python:3.9-slim

WORKDIR /app

# Install flask
RUN pip install flask

COPY app.py .

CMD ["python", "app.py"]