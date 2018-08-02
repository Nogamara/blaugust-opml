
output/blaugust.opml:
	@rm cache/_out
	python opml.py input.txt | tee cache/_out | grep -v "^#" > output/blaugust.opml
	cat cache/_out | grep "^# http" | sed 's/^# //g' | sort  > output/blaugust.txt

deps:
	pip install requests
	pip install beautifulsoup4

.PHONY: deps output/blaugust.opml
