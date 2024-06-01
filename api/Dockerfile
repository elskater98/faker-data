FROM python:3.10-alpine3.19
LABEL org.opencontainers.image.source=https://github.com/elskater98/fake-data
LABEL org.opencontainers.image.description="Fake Data Project"
LABEL org.opencontainers.image.licenses=MIT
ARG FLASK_ENV=production

ENV FLASK_ENV=${FLASK_ENV}

WORKDIR /app
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY app.py app.py
COPY error_handler.py error_handler.py
COPY routes routes

EXPOSE 8080

CMD ["gunicorn", "-w" ,"4" ,"-b" ,"0.0.0.0:8080", "app:create_app()"]