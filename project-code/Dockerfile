FROM python:3-onbuild


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

RUN pip install pandas, numpy, scipy, scikit-learn
# RUN git clone git://github.com/yyuu/pyenv.git .pyenv
# RUN git clone https://github.com/yyuu/pyenv-virtualenv.git ~/.pyenv/plugins/pyenv-virtualenv
# RUN pyenv install 3.6.4
COPY . /app

WORKDIR /app


EXPOSE 8080
#CMD ["python regressionAPI.py"]
