import sys
import json
from metadata_dict import *


def print_usage():
	print "python generate_dict.py <path_to_output_json_file>"

if(len(sys.argv) < 2):
	print_usage()
	sys.exit()

print "opening..."+sys.argv[1]

try:
	f = open(sys.argv[1], 'w')
except Exception, e:
	print "Exception " + str(e)
	sys.exit()


tuple_list = {}


#
# Add stuff here
#

location_list = {
	"bedroom",
	"living room",
	"hall",
	"kitchen",
	"bathroom"
}

obj_list = {
	"fan",
	"heater",
	"light",
	"bulb"
}

action_list = {
	"turn off",
	"switch off",
	"turn on",
	"switch on"
}

state_list = {
	"on",
	"off",
}

tuple_list[STRING_LOCATION] = location_list
tuple_list[STRING_OBJECT] = obj_list
tuple_list[STRING_ACTION] = action_list


def set_default(obj):
	if isinstance(obj, set):
		return list(obj)

	raise TypeError


try:
	json_str = json.dumps(tuple_list, default=set_default)
except Exception, e:
	print "Exception " + str(e)
	sys.exit()


print json_str

f.write(json_str)
f.close()