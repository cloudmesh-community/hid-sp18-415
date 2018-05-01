From heroku/miniconda

# Grab requirements.txt
ADD ./project/requirements.txt /tmp/requirements.txt

#Install dependencies
RUN pip install -qr /tmp/requirements.txt

#add code
ADD ./project/opt/regrapp/
WORKDIR /opt/regrapp

RUN conda install pandas scikit-learn


cmd gunicorn --bind 0.0.0.0:$PORT wsgi
