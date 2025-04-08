FROM python:3.9-slim
WORKDIR /app
COPY . .
COPY templates/ ./templates/
RUN pip install -r requirements.txt
CMD ["python", "app.py"]
