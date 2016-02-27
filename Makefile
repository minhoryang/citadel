pex: citadel.pex

egg:
	python setup.py sdist
	pip download -r requirements.txt -d dist/

citadel.pex: egg requirements.txt
	pex -o citadel.pex  --no-pypi -f dist/  -m citadel.citadel  -r requirements.txt citadel

clean:
	rm -rf citadel.egg-info build/ dist/ citadel.pex citadel/__pycache__/ ~/.pex/build/
