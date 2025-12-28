from python:3.11-slim
WORKDIR /app

copy Backend/requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY Backend/app ./app

ENV PYTHONPATH=/app

CMD ["uvicorn","app.main:app","--host","0.0.0.0","--port","10000"]
