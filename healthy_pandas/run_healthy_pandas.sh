#!/bin/bash

SCRIPT_DIR=$(dirname "$0")
source "$SCRIPT_DIR/.venv/bin/activate"

python "$SCRIPT_DIR/healthy_pandas.py" "$1"

deactivate