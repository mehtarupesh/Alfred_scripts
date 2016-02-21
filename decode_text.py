import sys
import json
from metadata_dict import *

def print_usage():
	print "python decode_text.py <path_to_text_file> <path_to_json_dictionary>"


def parse_command(json_dict, line):

	tuple_list = {}
	location_list = {}
	obj_list = {}
	action_list = {}

	print "Command = " + line
	tuple_list = json.loads(json_dict)

	location_list = tuple_list[STRING_LOCATION]
	obj_list = tuple_list[STRING_OBJECT]
	action_list = tuple_list[STRING_ACTION]

	location_val = "error"
	object_val = "error"
	action_val = "error"

	for item in location_list:
		if item in line:
			location_val = item
			break

	for item in obj_list:
		if item in line:
			object_val = item
			break

	for item in action_list:
		if item in line:
			action_val = item
			break	

	print "Location : " + location_val
	print "Object   : " + object_val
	print "Action   : " + action_val


if(len(sys.argv) < 3):
	print_usage()
	sys.exit()

print "Opening..." + sys.argv[1]

try:
	f = open(sys.argv[1])
except Exception, e:
	print "Exception " + str(e)
	sys.exit()

try:
	json_dict = open(sys.argv[2])
except Exception, e:
	print "Exception " + str(e)
	sys.exit()

str_dict = json_dict.read()

for line in f:
	parse_command(str_dict, line)
