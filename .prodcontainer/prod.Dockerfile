FROM python:3.9
RUN apt-get update && apt-get -y upgrade

COPY . /workspace
WORKDIR /workspace

RUN /usr/local/bin/python -m pip install --upgrade pip
RUN pip install --no-cache-dir pipenv
RUN pipenv install --dev --system
