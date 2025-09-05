FROM python:3.11.13
COPY ./ .
RUN pip install -r requirements.txt
