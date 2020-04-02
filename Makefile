
output/blapril2020/blaugust.opml:
	@-rm cache/_out_blapril2020
	@mkdir -p output/blapril2020
	python opml.py input.txt | tee cache/_out_blapril2020 | grep -v "^#" > output/blapril2020/blaugust.opml
	cat cache/_out_blapril2020 | grep "^# http" | sed 's/^# //g' | sort  > output/blapril2020/blaugust.txt

output/blaugust.opml:
	@-rm cache/_out
	@mkdir -p output
	python opml.py input.txt | tee cache/_out | grep -v "^#" > output/blaugust.opml
	cat cache/_out | grep "^# http" | sed 's/^# //g' | sort  > output/blaugust.txt

deps:
	pip install requests
	pip install beautifulsoup4

.PHONY: deps output/blaugust.opml
