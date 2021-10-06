FROM ubuntu:18.04

RUN apt-get update -y \

&& apt-get install python3-pip python3-dev libpq-dev -y \

&& apt-get install vim -y

WORKDIR /src/backend

COPY requirements.txt /src/backend/

RUN pip3 install -r requirements.txt

COPY . /src/backend/

EXPOSE 8000

ENTRYPOINT ["sh", "entrypoint.sh"]