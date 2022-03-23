FROM python:3.7-alpine

RUN mkdir /app
WORKDIR /app
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY . /app
EXPOSE 8000
CMD ["python","acervo.py"]