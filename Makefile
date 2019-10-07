test:
	python3 access.py -au daniel 1234
	python3 access.py -au rafay 1234
	python3 access.py -a rafay 1234
	python3 access.py -a daniel 1234
	python3 access.py -autg project daniel
	python3 access.py -autg daniel project
	python3 access.py -autg rafay project
	python3 access.py -aotg laptop backpack
	python3 access.py -aotg pen backpack
	python3 access.py -aa use project backpack
	python3 access.py -ca use rafay laptop
	python3 access.py -ca use rafay tv
	python3 access.py -ca use daniel pen Can Access

clean:
	rm *.txt
