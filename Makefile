# Makefile for Beburos (Git Bash compatible)

install:
	py -3.11 -m venv venv311 && source venv311/Scripts/activate && pip install -r requirements.txt

run:
	source venv311/Scripts/activate && python main.py --mode app

clean:
	rm -rf venv311
	find . -name "*.pyc" -delete
	rm -rf __pycache__

