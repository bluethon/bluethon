.PHONY: .ONESHELL

.ONESHELL:

SHELL=/bin/bash
.DEFAULT_GOAL := start

%: export COMPOSE_PROJECT_NAME =

### common

clean-image:
	docker-compose down --rmi local
prune:
	docker image prune -f --filter until=240h

### deploy

clean-volume:
	docker-compose down -v

CMD=-h

test:
	docker-compose ${CMD}

pull:
	docker-compose pull

down:
	docker-compose down

build:
	docker-compose build

up:
	docker-compose up -d

up-%:
	echo $${COMPOSE_FILE}
	docker-compose up -d --no-dep $*

start: down build up
