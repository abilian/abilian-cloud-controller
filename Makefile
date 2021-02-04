.PHONY: test setup-env install check clean tidy

test:
	poetry run acc/main.py halt
	poetry run acc/main.py clean
	poetry run nosetests -v

check:
	poetry run pep8 --exclude env -r --ignore E111,E225,E501 .
	poetry run pylint -d W0311 acc

clean:
	find . -name "*.pyc" | xargs rm -f
	rm -rf build acc.egg-info dist
	poetry run acc/main.py halt
	poetry run acc/main.py clean

tidy: clean
	rm -rf .tox

push:
	echo "Not yet"
	#rsync -avz -e ssh src Makefile dependencies.txt crawl.sh \
	#	xxx@yyy.abilian.com:/var/www/home.abilian.org/
