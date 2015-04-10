.PHONY: test
test:
	nosetests -s --cover-package=. --nologcapture --cover-erase --cover-tests --cover-branches


.PHONY: clean
clean:
	rm -rf build dist limbo.egg-info .env .coverage limbo.sqlite3

.PHONY: run
run: install
	bin/limbo

.PHONY: repl
repl: install
	bin/limbo -t

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
	flake8 limbo test
