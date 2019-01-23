#------------------------------
# By Fahad Alduraibi
# Last update: June 12, 2012
# Version: 1.1
# modified by VDE
# on November 12,2018
#------------------------------

import mechanize
import sys

br = mechanize.Browser()
br.set_handle_equiv(True)
#br.set_handle_gzip(True)
br.set_handle_redirect(True)
br.set_handle_referer(True)
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
br.addheaders = [('User-agent', 'Mozilla/5.0 (X11; Linux x86_64; rv:13.0) Gecko/20100101 Firefox/13.0')]

testURL = 'https://test.html'
response = br.open(testURL)
print ("----------------------------")
print (" Automatic Login to  portal starting")
if __debug__:

	print ("RESPONSE TO : ",testURL)
	print response.read()
	print ("----------------------------------")

if response.geturl() == testURL:
	print "You are already logged in to wifi."
	sys.exit()



# new api for HTML5
forms=list(br.forms())
if __debug__:
	print ("FIRST FORM RECEIVED : ")
	print forms[0]
	print ("----------------------------------")


	
# process form
form = forms[0]
request = form.click()
#
# this response needs to be processed  as final redirection

antwoord = br.open(request)

#response = mechanize.urlopen(request)
#print ("response to form : ")
#print response.read()
#print response

forms=list(br.forms())

if __debug__:
	print ("SECOND FORM RECEIVED :")
	print forms[0]
	print ("-----------------------------------")

form = forms[0]
request = form.click()
# adding a try session in case connection is already granted
# close app without crashing
try:
	# 
	response = mechanize.urlopen(request)
except:
	response.close()
	sys.exit()
if __debug__:
	print ("RESPONSE SECOND FORM PROCESSED : ")
	print response.read()
	print ("-----------------------------------")

response.close()
print "--- WIFI  Login Done ---"
