From heroku/miniconda

# Grab requirements.txt
ADD ./regapp/requirements.txt /tmp/requirements.txt

#Install dependencies
RUN pip install -qr /tmp/requirements.txt

#add code
ADD ./regapp /opt/regrapp/
WORKDIR /opt/regapp

RUN conda install pandas scikit-learn


CMD gunicorn --bind 0.0.0.0:$PORT wsgi
