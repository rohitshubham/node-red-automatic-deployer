FROM python:3.7-alpine

# Create the workspace
WORKDIR /code

# Install dependency for the wait-for script
RUN apk update && apk add --no-cache netcat-openbsd

# Install dependency on original code
RUN pip3 install requests
COPY . .

CMD ["python3", "app.py"]