FROM python:3.7-alpine
WORKDIR /code
RUN apk update && apk add --no-cache netcat-openbsd
RUN pip3 install requests
COPY . .
CMD ["python3", "app.py"]