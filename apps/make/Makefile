.PHONY: all check clean

objects = $(wildcard *.in)
outputs := $(objects:.in=.txt)

all: $(outputs)

%.txt: %.in
	pip-compile -v --output-file $@ $<

test.txt: base.txt

check:
	@which pip-compile > /dv/null

clean: check
	- rm *.txt

dc: requirements/dev.in
	pip-compile -v -o requirements/dev.txt requirements/dev.in
ds: requirements/dev.txt
	pip-sync requirements/dev.txt

cc: requirements/common.in
	pip-compile -v -o requirements/common.txt requirements/common.in
cs: requirements/common.txt
	pip-sync requirements/common.txt


f: s
	echo '123'
s:
	# 命令前加- 可以忽略失败继续执行, 另外可以make -k
	-docker volume ls | grep datavisualizationfrontend_node1
