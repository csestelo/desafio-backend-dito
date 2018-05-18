#!/bin/sh

#PYTHONPATH="$(pwd):$PYTHONPATH"

PYTHONPATH=. python script/populate_db.py && python -m api