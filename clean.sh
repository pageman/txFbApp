#!/bin/sh
#
# Copyright (c) 2012 Enrique Samson Jr. <enriquejr at gmail dot com>
#
# Distributed under the MIT License (See accompanying LICENSE.txt)
#

find ./ -name "*.pyc" | xargs rm -f
find ./ -name "*~" | xargs rm -f
find ./ -name "dropin.cache" | xargs rm -f
find ./ -name "_trial_temp" | xargs rm -rf
find ./ -name "*.log" | xargs rm -rf
find ./ -name "*.log.*" | xargs rm -rf

