## Flask API to Get Regression Details and Post Prediction

* There are two API endpoints and two request methods, GET and POST
   
   * ```/currentDetails```
  
   * ```/predict```
  
## Instructions for running in Docker

* Install Docker ce

* git clone https://github.com/cloudmesh-community/hid-sp18-415/tree/master/project-code

* Build Docker Image
  
    ```sudo docker-build```
   
* start the service with any of the following commands

   * ```make```
   
   * ```run```
   
   * ```make docker-start```
   
* Test Service by running following commands
   
   * ```curl -H "Content-Type: application/json" -X GET -d ''http://localhost:5000/currentDetails```
    
   * ```curl -H "Content-Type: application/json" -X POST -d ''http://localhost:5000/predict```
   
* Stop Service running command:
   
   * ```make docker-stop```    

