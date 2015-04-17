.PHONY: all
all: clean run

.PHONY: test
test:
	nosetests --with-coverage -s --cover-package=. --nologcapture --cover-erase --cover-tests --cover-branches

.PHONY: clean
clean:
	scripts/clean.sh TOKEN

.PHONY: run
run: install
	scripts/get_token.sh
	bin/Slashchat

.PHONY: run_circle
run_circle: install
	bin/Slashchat

.PHONY: repl
repl: install
	scripts/get_token.sh
	bin/Slashchat -t

.PHONY: install
install:
	easy_install -U pip
	pip install -r requirements.txt --upgrade
	python setup.py install
	make clean

.PHONY: publish
publish:
	pandoc -s -w rst README.md -o README.rs
	python setup.py sdist upload
	rm README.rs

.PHONY: flake8
flake8:
	flake8 Slashchat test

TOKEN:  
	scripts/get_token.sh
