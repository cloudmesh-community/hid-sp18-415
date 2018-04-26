FROM ubuntu:16.04


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

RUN git clone git://github.com/yyuu/pyenv.git .pyenv
RUN git clone https://github.com/yyuu/pyenv-virtualenv.git ~/.pyenv/plugins/pyenv-virtualenv
RUN pyenv install 3.6.4
RUN git clone https://github.com/cloudmesh-community/hid-sp18-415.git
WORKDIR hid-sp18-415/hid-sp18-415/project-code

RUN mkdir -p cloudmesh-regressionAPI
RUN mkdir -p ~/.cloudmesh

Run pip install pandas
RUN pip install numpy, Scipy, SciKit-learn

EXPOSE 8080
CMD ["python regressionAPI.py"]
