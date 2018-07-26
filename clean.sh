#!/bin/bash
# -*- coding: utf-8 -*-
#
# Description   : Clean the workspace and all the caches
# Author        : FakeCola
# Date          : Jul 25, 2018
#=============================================

reset

# clean pyc files
find . -name '*.pyc' -type f -delete

# clean book caches
pushd ./lmf
dump_path=$(python conf.py "DUMP_HOME")
rm -rf $dump_path
popd

echo "Done" && exit 0
