.PHONY: test
test:
	nosetests --with-coverage -s --cover-package=. --nologcapture --cover-erase --cover-tests --cover-branches

.PHONY: clean
clean:
	rm -rf `cat .gitignore`

.PHONY: run
run: install TOKEN
	export SLACK_TOKEN=`cat TOKEN`
	bin/limbo
	make clean

.PHONY: repl
repl: install TOKEN
	export SLACK_TOKEN=`cat TOKEN`
	bin/limbo -t
	make clean

.PHONY: install
install:
	easy_install -U pip
	pip install -r requirements.txt --upgrade
	python setup.py install

.PHONY: publish
publish:
	pandoc -s -w rst README.md -o README.rs
	python setup.py sdist upload
	rm README.rs

.PHONY: flake8
flake8:
	flake8 limbo test

TOKEN:  
	./get_token