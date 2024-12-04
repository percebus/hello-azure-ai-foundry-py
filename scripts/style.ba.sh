#!/bin/bash

set -e
set -x

npx prettier . --write
ruff check . --fix

set +x
set +e
