FROM python:3.10.0-alpine

WORKDIR /app

ENV "OPEN_AI_KEY"="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"

COPY src/ /app/src
COPY requirements.txt /app

RUN pip install --upgrade pip && pip install -r requirements.txt

EXPOSE 8000

CMD ["uvicorn", "src.main:app", "--reload", "--host", "0.0.0.0", "--port", "8000"]