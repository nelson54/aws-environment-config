FROM python:3.12.0b3-slim-bookworm
RUN apt update && apt install -y git
WORKDIR /usr/src/app

COPY requirements.txt ./

COPY ./* ./

RUN pip install --no-cache-dir -r requirements.txt

FROM python:3.12.0b3-slim-bookworm

CMD python3 -m ./__main__.py