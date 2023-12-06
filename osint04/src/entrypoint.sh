#!/bin/bash

set -ex

cd /var/www/html/ && bundler exec jekyll serve &
tor