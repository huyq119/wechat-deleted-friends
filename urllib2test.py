# coding=utf-8
import urllib2
response = urllib2.urlopen('https://testerhome.com')
htmltest = response.read().decode('utf-8')
print htmltest
