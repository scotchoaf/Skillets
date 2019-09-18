#!/usr/bin/env python3
#
# This example uses ENV variables to gather input from the user
# The .meta-cnc file defines 3 input variables:
# USERNAME, PASSWORD, SECRET
# This script shows how to obtain the values entered from the user
#
import json
import os
import sys

from skilletlib.exceptions import LoginException
from skilletlib.exceptions import SkilletLoaderException
from skilletlib.panoply import Panoply

# each variable will be present in the environ dict on the 'os' module
username = os.environ.get('TARGET_USERNAME', 'admin')
password = os.environ.get('TARGET_PASSWORD', 'admin')
ip = os.environ.get('TARGET_IP', '')
from_candidate = os.environ.get('FROM_CANDIDATE', 'False')

# check if we should generate the skillet from the candidate of the running config
if from_candidate == 'True':
    fc = True
else:
    fc = False

snippets = list()

try:
    device = Panoply(hostname=ip, api_username=username, api_password=password)
    snippets = device.generate_skillet(from_candidaate=fc)
    print(json.dumps(snippets, indent=2))
    sys.exit(0)

except SkilletLoaderException as se:
    print('Error Executing Skillet')
    print(se)
    sys.exit(1)
except LoginException as le:
    print('Error Logging into device')
    print(le)
    sys.exit(1)

