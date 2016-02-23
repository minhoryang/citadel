pex: citadel.pex

egg:
	python setup.py sdist
citadel.pex: egg requirements.txt
	pex -o citadel.pex -r requirements.txt -f dist -m citadel.citadel

clean:
	rm -rf citadel.egg-info build/ dist/ citadel.pex
