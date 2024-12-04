#!/bin/bash

set -e
set -x

python -m pip freeze > requirements.frozen.txt

set +x
set +e
