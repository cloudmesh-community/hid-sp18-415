PROJ_NAMe=jmudvari@iu.edu

run:
	python regressionAPI.py
docker-build:
	docker build -t ${PROJ_NAME} .
docker-start-background:
	docker run -d -p 5000:5000 ${PROJ_NAME}
docker-start-int:
	docker run -d -p 5000:5000 ${PROJ_NAME}
docker-stop:
	docker stop $$(docker ps -a -q --filter ancestor=$(PROJ_NAME))
