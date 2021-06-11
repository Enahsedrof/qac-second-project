FROM python:latest
WORKDIR /app
COPY . .
RUN pip3 install -r requirements.txt
EXPOSE 5003
ENTRYPOINT [ "python3", "app.py" ]