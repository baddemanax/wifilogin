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

testURL = 'https://guest.cis.consilium.europa.eu/guest/portal.php'
response = br.open(testURL)
print ("response url : ")
print response.read()

if response.geturl() == testURL:
	print "FAD: You are already logged in to council eu."
	sys.exit()

try:
	forms = mechanize.ParseResponse(response, backwards_compat=False)
	print ("forms received : ")
	print forms[0]
except:
	print "FAD: Error in parsing forms, Am I already logged in?"
	sys.exit()

	response.close

form = forms[0]
print (" form to answer : ")
print form
#print "----------------------------------- Login"
request = form.click()
response = mechanize.urlopen(request)
print ("response to form : ")
print response.read()
#try:
forms = mechanize.ParseResponse(response, backwards_compat=False)
print ("second forms :")
print forms[0]
#except:
print(" error in parsing second form ")
#
sys.exit()
#response.close

form = forms[0]
request = form.click()
response = mechanize.urlopen(request)
print ("response 2 to form : ")
print response.read()
try:
	forms = mechanize.ParseResponse(response, backwards_compat=False)
	print ("last forms :")
	print forms[0]
except:
	print (" error while opening last form ")
	response.close()
response.close()
print "--- council eu Done ---"
