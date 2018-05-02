From heroku/miniconda

# Grab requirements.txt
ADD ./regapp/requirements.txt /tmp/requirements.txt

#Install dependencies
RUN pip install -qr /tmp/requirements.txt

#add code
ADD ./regapp /opt/regapp/
WORKDIR /opt/regapp

RUN conda install pandas scikit-learn


CMD gunicorn -w 4 -b 127.0.0.1:5000 regressionAPI:app 
