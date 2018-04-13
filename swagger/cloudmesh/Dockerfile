From ubuntu:16.04
Maintainer Janaki Mudvari Khatiwad

RUN apt-get update -q

RUN pyenv python 3.6.4

RUN git clone https://github.com/cloudmesh-community/hid-sp18-415.git

WORKDIR /hid-sp18-417/swagger/cloudmesh/identity

EXPOSE 8080
RUN make service
CMD ["make", "start"]
