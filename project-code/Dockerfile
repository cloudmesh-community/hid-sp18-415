FROM python:3-onbuild
RUn apt-get update

RUN apt-get install -q -y net-tools
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt

EXPOSE 5000

ENTRYPOINT ["make", "run"]
