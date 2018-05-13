#!/bin/sh

PYTHONPATH=$(pwd):$PYTHONPATH

python script/populate_db.py && python -m api