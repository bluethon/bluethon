.PHONY: start .ONESHELL

.ONESHELL:

SHELL=/bin/bash
.DEFAULT_GOAL := start

#%: export COMPOSE_PROJECT_NAME =
#%: export COMPOSE_FILE := docker-compose.dev.yml
#%: export COMPOSE_FILE = docker-compose.yml:docker-compose.init.yml
#%: export COMPOSE_FILE = docker-compose.dev.yml:docker-compose.init.dev.yml

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

build: clean-image
	docker-compose build

down:
	docker-compose down

up:
	docker-compose up -d

up-%:
	echo $${COMPOSE_FILE}
	docker-compose up -d --no-dep $*

start: stop build up
