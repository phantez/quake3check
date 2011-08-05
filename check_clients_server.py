#!/usr/bin/python
import quake3check
from time import localtime, strftime

IP="127.0.0.1"
PORT=27960
TIMEOUT=5

dresp, err = quake3check.interogate(IP,PORT,TIMEOUT)
ldate =strftime("%Y-%m-%d-%H:%M:%S", localtime())
if err != False:
	print "%s : %s" % (ldate, err)
else:
	print "%s\t%s" % (ldate, dresp["clients"])
