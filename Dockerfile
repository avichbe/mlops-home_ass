FROM python:3.9-slim

WORKDIR /app
EXPOSE 5000
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

CMD ["python", "src/app.py"]