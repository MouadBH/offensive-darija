.PHONY: run
run:
	docker-compose -f docker-compose.yml up

.PHONY: build
build:
	docker-compose -f docker-compose.yml build

.PHONY: web
web:
	docker exec -it web bash

.PHONY: down
down:
	docker-compose -f docker/docker-compose.yml down -v

.PHONY: reset
reset:
	docker stop $(docker ps -q); docker rm $(docker ps -a -q)

.PHONY: prune
prune:
	docker network prune -f; docker volume prune -f

.PHONY: kill
kill:
	make down; make reset; make prune; make run