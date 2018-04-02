# Heroku

## Overview

* Platform as a service(Paas)
* Build on top of Amazon Web Services(AWS, EC2)
  Heroku servers are hosted on AWS. 
* Partly open source and partly commercial
* Owned by Salesforce 
* Developer friendly

  Developers write their API locally and can deploy
  to Heroku through git or GitHub.

## Features

* Languages

  - Node, Ruby, PHP, Go, Scala, Python, Java, Clojure are the
    languages supported by Heroku but it supports any other languages
    through Add-Ons and Buildpacks.This feature make it language
    friendly.

* Database services
  - Postgres and Redis are supported
* Heroku Connect
  - Data in Postgres can be synchronized to the database of Salesforce
    organizations
 * Heroku Enterprise
   - It provides private spaces and access control features to large
     enterprises to collaborate and manage api resources,users and
     development
 * Heroku Teams
   - Collaboration platform for application management and
     development.
 * Dynos
   - Virtual Linux Containers/Servers
   - More info [Here](https://github.com/cloudmesh-community/hid-sp18-415/blob/master/paper/content.tex/)
 * Heroku Elements
 * Command line Interface(CLI)
   Download Heroku CLI to create and manage apps directly from the terminal.
   - On macos [Link](https://cli-assets.heroku.com/heroku-cli/channels/stable/heroku-cli.pkg)
   - On Windows 
      [!64-bit installer](https://cli-assets.heroku.com/heroku-cli/channels/stable/heroku-cli-x64.exe/) 
      [!32-bit installer](https://cli-assets.heroku.com/heroku-cli/channels/stable/heroku-cli-x86.exe/)
      
    - Ubuntu/Debian run following command
     ```sh
     $ wget -qO- https://cli-assets.heroku.com/install-ubuntu.sh | sh 
     $ sudo snap install heroku --classic  for Ubuntu snap
     
     ```
   - To verify CLI installation, type

     ```sh
     $ heroku version
     ```

## Architecture [Here in Detail](https://github.com/cloudmesh-community/hid-sp18-415/blob/master/paper/content.tex/)
 
* Source codes developed in local terminal 
* requirements.txt file with all the dependencies
* Procfile a text file with info on application process types
* Slug, bundle of source code, requirements.txt and Procfile 
* Config Vars, environmental variables
* Release, combination of slug and config vars
* Dyno manager
* Add-ons
* Heroku logs
* HTTP routing 

## API with Python Flask on Heroku (incomplete, working on it)

* Download flask and gunicorn, virtualenv or pyenv if we don't have
  setup already
* Define or create info.py file, e.g.,
 
   ```sh
   from flask import Flask

   app = Flask(__name__)

   @app.route('/')

   def index():
       return "my app info!"

   if __name__ =="__main__":
       app.run()
   ```
* Run pip freeze > requirements.txt to install dependencies
* Define Procfile with process specification, web is a process in this example
     ```sh
     web: gunicorn info:app
     ```
* Heroku CLI should be installed
* Run heroku login and login to heroku account to autenticate, if you do not have one, create one
* Go to app directory
* Run gitinit to initiate a git repository
* Git add, git commit and Push will push info.py, requirements.txt and
  Procile
* Heroku now compiles info.py, Procfile and the dependencies from
  requirements.txt into a bundle called ``slug''
* Type command create Heroku that will create herokuapp.com and also
  gives us the url of our app
* run heroku open, opens app url

 

