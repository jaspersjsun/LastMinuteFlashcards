#!/bin/bash
# -*- coding: utf-8 -*-
#
# Description   : Clean the workspace, remove caches and logs
# Author        : FakeCola
# Date          : Jul 25, 2018
#=============================================

reset

# clean pyc files
find . -name '*.pyc' -type f -delete
find . -name '__pycache__' -type d -delete

pushd ./lmf

# clean book caches
dump_path=$(python conf.py "DUMP_HOME")
rm -rf $dump_path

# clean logs
log_path=$(python conf.py "LOG_PATH")
rm -rf $log_path

popd

echo "Done" && exit 0
