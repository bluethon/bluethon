.PHONY: .ONESHELL build test up down start

.ONESHELL:

SHELL=/bin/bash
.DEFAULT_GOAL := start

%: export COMPOSE_PROJECT_NAME =

pull down build ps:
	docker-compose $@

CMD=-h
test:
	docker-compose ${CMD}
clean-volume:
	docker-compose down -v

up:
	docker-compose up -d
up-%:
	echo $${COMPOSE_FILE}
	docker-compose up -d --no-dep $*

start: build down up
