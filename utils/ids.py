#!/usr/bin/env python

import sys
import json
import fileinput
import dateutil.parser

for line in fileinput.input():
    try:
        tweet = json.loads(line)
        print tweet["id_str"]
    except Exception as e:
        sys.stderr.write("uhoh: %s\n" % e)




