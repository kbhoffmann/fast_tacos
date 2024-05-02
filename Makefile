docker-up-local:
	docker-compose -f setup/docker-compose-local.yml up -d
	docker logs taco_web -f

docker-down-local:
	docker-compose -f setup/docker-compose-local.yml down
