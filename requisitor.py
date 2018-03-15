#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Author: David Samuel
# Version 1.0

from conf import get_file_name
from util import create_log_file
from logsaver import to_save
import requests

try:

	create_log_file()

	f = open("files/" + get_file_name(), "r")

	counter = 1

	for line in f.readlines():

		print str (counter) + "- " + line.strip()

		response = requests.get('http://www.server.com/files/'+line.strip())

		if response.status_code != 200:
			
			to_save(line.strip())

		counter += 1

	f.close()

except requests.exceptions.ConnectionError:
	print "Connection error"
except IOError:
	print "File or directory does not exist"
finally:
	print "Finished"
