#!/bin/bash

set -e
set -x

npx prettier . --check
ruff check .

set +x
set +e
