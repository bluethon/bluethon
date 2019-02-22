.PHONY: all check clean .ONESHELL

.ONESHELL:

SHELL=/bin/bash
.DEFAULT_GOAL := start

clean-volume:
	docker-compose down -v

CMD=-h

test:
	docker-compose ${CMD}

down:
	docker-compose down

build:
	docker-compose build

up:
	docker-compose up -d

start: down build up

up-%:
	echo $${COMPOSE_FILE}
	docker-compose up -d --no-dep $*
