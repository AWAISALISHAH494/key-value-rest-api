FROM python:3.11-slim AS builder

WORKDIR /app


RUN apt-get update && apt-get install -y \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .

RUN pip3 install  --no-cache-dir -r requirements.txt


FROM gcr.io/distroless/python3-debian12

WORKDIR /app


COPY --from=builder /usr/local/lib/python3.11/site-packages /usr/local/lib/python3.11/site-packages
COPY --from=builder /usr/local/bin/uvicorn /usr/local/bin/uvicorn

ENV PYTHONPATH=/usr/local/lib/python3.11/site-packages
 
COPY . .

EXPOSE 2000

CMD [ "/usr/local/bin/uvicorn","app.main:app","--reload", "--host","0.0.0.0","--port","2000" ] 