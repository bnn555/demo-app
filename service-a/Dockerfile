# syntax=docker/dockerfile:1

FROM python:3.10-slim-bullseye

WORKDIR /service-a

COPY ./requirements.txt /service-a/requirements.txt

RUN pip3 install -r requirements.txt

COPY . /service-a/

ENTRYPOINT [ "python" ]

CMD ["btc-price.py" ]