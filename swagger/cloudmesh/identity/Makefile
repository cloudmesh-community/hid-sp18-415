# assumes swager_codegen environment variable contains
# the path to swagger codegen jarfile


SPEC=identity.yml
SERVERDIR=server/
DESTDIR=server/identity/flaskConnexion
SERVICE_NAME=cloudmesh_identity_service
swagger_codegen=java -jar swagger-codegen-cli.jar

all: service start
	@echo "service started"


fetch:
	wget https://oss.sonatype.org/content/repositories/releases/io/swagger/ 
	swagger-codegen-cli/2.3.1/swagger-codegen-cli-2.3.1.jar
	-O swagger-codegen-cli.jar

generate:
	$(swagger_codegen) generate \
		-i $(SPEC) \
		-l python-flask \
		-o server/identity/flaskConnexion \
		-D supportPython3=true 
	@echo "generated code"
	cp *_controller.py server/identity/flaskConnexion/swagger_server/controllers/  
	@echo "copied"

requirements:
	pip install -r requirements.txt; python setup.py install
	cd server/identity/flaskConnexion; pip install -r requirements$

run:
	cd server/identity/flaskConnexion/ &&\
	python -m swagger_server

stop:
	#stops the service
	ps -ef | grep swagger | grep -v "grep"| awk '{print $$2}' | xargs kill -9

clean:
	rm swagger-codegen-cli.jar
	rm -rf server/
	
container:
	sudo docker build -t cloudmesh-identity .
	sudo docker run -p 8080:8080 cloudmesh-identity 
