FROM ubuntu:16.04
# FROM python:3-onbuild


RUN  apt-get update -q
RUN  apt-get install -qy \
        build-essential \
	python-dev \
	python-pip \
	libssl-dev \
	zlib1g-dev \
	libbz2-dev \
	libreadline-dev \
	libsqlite3-dev \
	wget \
	curl \
	default-jre \
        software-properties-common -y \
        git -y
        
RUN apt-get install -q -y net-tools

RUN git clone git://github.com/yyuu/pyenv.git .pyenv
#RUN git clone https://github.com/yyuu/pyenv-virtualenv.git ~/.pyenv/plugins/pyenv-virtualenv

ENV HOME  /
ENV PYENV_ROOT /.pyenv
ENV PATH $PYENV_ROOT/shims:$PYENV_ROOT/bin:$PATH

RUN pyenv install 3.6.4
RUN pyenv global 3.6.4
RUN python -m ensurepip
RUN pip install --upgrade pip

# RUN pip install pandas, numpy, scipy, scikit-learn

COPY . /app


WORKDIR /app
RUN pip install -r requirements.txt

EXPOSE 8080

CMD ["/app/app/regressionAPI.py"]
