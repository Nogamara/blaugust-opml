blaugust: output/blaugust2021/blaugust.opml

output/blaugust2021/blaugust.opml:
	@-rm cache/_out_blaugust2021
	@mkdir -p output
	python opml.py input.txt | tee cache/_out_blaugust2021 | grep -v "^#" > output/blaugust2021/blaugust.opml
	cat cache/_out_blaugust2021 | grep "^# http" | sed 's/^# //g' | sort  > output/blaugust2021/blaugust.txt
	cat fixup.txt | grep -o -P 'xmlUrl="([^"]+)' | sed 's/xmlUrl="//'    >> output/blaugust2021/blaugust.txt

output/blapril2020/blaugust.opml:
	@-rm cache/_out_blapril2020
	@mkdir -p output/blapril2020
	python opml.py input.txt | tee cache/_out_blapril2020 | grep -v "^#" > output/blapril2020/blaugust.opml
	cat cache/_out_blapril2020 | grep "^# http" | sed 's/^# //g' | sort  > output/blapril2020/blaugust.txt

output/blaugust2018/blaugust.opml:
	@-rm cache/_out_blaugust2018
	@mkdir -p output/blaugust2018
	python opml.py input.txt | tee cache/_out_blaugust2018 | grep -v "^#" > output/blaugust2018/blaugust.opml
	cat cache/_out_blaugust2018 | grep "^# http" | sed 's/^# //g' | sort  > output/blaugust2018/blaugust.txt

deps:
	pip install requests
	pip install beautifulsoup4

.PHONY: deps blaugust
