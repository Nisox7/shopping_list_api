FROM python:3.10-alpine3.16

WORKDIR /app

COPY . .

RUN pip3 install -r /app/requeriments.txt

EXPOSE 10510

CMD ["python3" , "/app/app.py"]