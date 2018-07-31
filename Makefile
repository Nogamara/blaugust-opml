
output/blaugust.opml:
	python opml.py input.txt | grep -v "^#" > output/blaugust.opml

deps:
	pip install requests
	pip install beautifulsoup4

.PHONY: deps output/blaugust.opml
