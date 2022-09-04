# syntax=docker/dockerfile:1

FROM python:3.10-slim-bullseye

WORKDIR /service-b

COPY ./requirements.txt /service-b/requirements.txt

RUN pip3 install -r requirements.txt

COPY ./dummy-rest-api.py /service-b/dummy-rest-api.py

ENTRYPOINT [ "python" ]

CMD ["dummy-rest-api.py" ]
