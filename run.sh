#!/bin/bash
# Usage 
# ./run.sh RECIPE_FILE OUTPUT_NAME

python generate_json.py $1
webkit2png -F -z 2.8 --delay=2 -o $2 http://localhost:8000
