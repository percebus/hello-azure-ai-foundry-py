#!/bin/bash

target_config=$1
echo "target_config:'${target_config}'"

PIP_CLI_OPTS=""
requirements="requirements.txt"
if [[ "$target_config" == "release" ]]; then
    echo "Installing ONLY prd requirements..."
    requirements="requirements.release.txt"
else
    PIP_CLI_OPTS="-e"
    echo "Installing everything..."
fi

set -e
set -v

# always upgrade
python -m pip install --verbose --upgrade pip
python -m pip install --verbose --upgrade --requirement requirements.upgrade.txt

# install 1x
python -m pip install --verbose --requirement ${requirements}
python -m pip install --verbose ${PIP_CLI_OPTS} .

set +v
set +e
