FROM python:3.8.5-slim-buster

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

RUN pip install --upgrade pip
COPY requirements.txt ./
RUN pip install -r requirements.txt

COPY website/ ./

EXPOSE 8000
CMD ["uvicorn", "website.app:app", "--host=0.0.0.0", "--port=8000"]
