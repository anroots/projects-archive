#!/usr/bin/python -tt

# Send a message to a chatterbot and return it's reply.
# Author A.Roots

import urllib, urllib2
from xml.dom import minidom
from xml.sax.saxutils import unescape

class Robot:
    
    def __init__(self,robotName, robotId):
        self.robotName = robotName
        self.robotId = robotId
        self.currentConversation = ''

# Input: query
# Output: tuple (chatId, reply)    
    def pandabot(self, inputStr):
      
      base_url = 'http://www.pandorabots.com/pandora/talk-xml'
      data = urllib.urlencode([('botid', self.robotId), ('input', inputStr), ('custid', self.currentConversation)])
      
      # Submit POST data and download response XML
      req = urllib2.Request(base_url)
      fd = urllib2.urlopen(req, data)
      
      # Take Bot's response out of XML
      xmlFile = fd.read()
      dom = minidom.parseString(xmlFile)
      objektid = dom.getElementsByTagName('that')
      bot_response = objektid[0].toxml()
      bot_response = bot_response[6:]
      bot_response = bot_response[:-7]
      # Some nasty unescaping
      bot_response = unescape(bot_response, {"&apos;": "'", "&quot;": '"'})
      
      # Get the conversation ID
      currentId = dom.getElementsByTagName('result')
      reflist = currentId[0]
      chatId = reflist.attributes['custid']
      self.currentConversation = str(chatId.value)
      
      return str(bot_response)
