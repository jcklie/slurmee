test:
	python3 -m unittest

black:
	black -l 120 slurmee/
	black -l 120 tests/