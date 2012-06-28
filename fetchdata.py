#!/usr/bin/python

import json
import sys


destination = '../data'
username = sys.argv[1]

alltags_url = 'http://feeds.delicious.com/v2/json/tags/%s'


print username
