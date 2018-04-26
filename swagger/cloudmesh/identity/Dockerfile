From ubuntu:16.04
Maintainer Janaki Mudvari Khatiwada

RUN apt-get update -q && apt-get install -qy \
build-essential \
    python-dev \
    python-pip \
    libssl-dev \
    zlib1g-dev \
    libbz2-dev \
    libreadline-dev \
    libsqlite3-dev \
    pandoc \
    wget \
    curl \
    git-core \
software-properties-common -y
RUN apt-get install -q -y net-tools

RUN git clone git://github.com/yyuu/pyenv.git .pyenv
RUN git clone https://github.com/yyuu/pyenv-virtualenv.git ~/.pyenv/plugins/pyenv-virtualenv

ENV HOME  /
ENV PYENV_ROOT /.pyenv
ENV PATH $PYENV_ROOT/shims:$PYENV_ROOT/bin:$PATH

RUN pyenv python 3.6.4

RUN git clone https://github.com/cloudmesh-community/hid-sp18-415.git

WORKDIR /hid-sp18-417/swagger/cloudmesh/identity
RUN wget https://oss.sonatype.org/content/repositories/releases/io/swagger/swagger-codegen-cli-2.3.1/swagger-codegen-cli-2.3.1.jar

RUN pip install -r requirements.txt
ENTRYPOINT [python 3.6.4]

EXPOSE 8080

CMD ["python -m swagger_server"]
