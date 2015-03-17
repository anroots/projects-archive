#!/usr/bin/python

from pandarobots import Robot
from xgoogle.translate import Translator
from xgoogle.translate import LanguageDetector
import sys, time, random, re, os

# <CONFIG>
robot1Name = 'Getter'
robot2Name = 'Mihkel'
logFileName = 'Conversation_log.txt' # Name of the logfile. Leave empty to skip.
conversationLimit = 100 # Both robots speak X times and the program will exit
# </CONFIG>

def main():
      
    translate = Translator()
    #1) the name of a robot 2) the robot ID as seen in www.pandarobots.com
    getter = Robot(robot1Name, 'ebbf27804e3458c5')
    mihkel = Robot(robot2Name, '923c98f3de35606b')

    # Deal with command-line arguments
    try:
        if sys.argv[1] == '--help':
            print 'Talky-AI by A.Roots'
            print '2 AI-s having a conversation. You must feed them a conversation-starter IN ENGLISH.'
            print 'The AI-s will speak in English, but you can have Google translate it into a suitable language.'
            print 'Just give the language code as a parameter.'
            print 'For a list of available language codes use ./talky-AI.py --languages'
            print 'Example: ./talky-AI.py fi'
        
        elif sys.argv[1] == '--languages':
            l_list = ''
            for item in translate.languageList():
                l_list = l_list + ',' + item
            l_list = l_list[1:]
            print 'Available language codes:'
            print l_list
            sys.exit(0)
        
        if sys.argv[1] in translate.languageList():
            transInto = sys.argv[1]
        else:
            transInto = 'en'
    except IndexError, e:
        transInto = 'en'
    
    # AI's need a seed to get the conversation going
    seedStr = raw_input('Enter a topic: ')
    if os.path.isfile(logFileName):
            os.unlink(logFileName)
    # Just keep repeating this stuff
    c = 0  
    while c < conversationLimit:
        # Getter's bit
        seedStr = getter.pandabot(seedStr)
        # Shorten response
        if len(seedStr) > 100:
            seedStr = shorten(seedStr)
        # Output
        output(unicode(translate.translate(seedStr,transInto,'en')),getter.robotName,1)
        
        # Mihkel's bit
        seedStr = mihkel.pandabot(seedStr)
        # Shorten response
        if len(seedStr) > 100:
            seedStr = shorten(seedStr)
        # Output
        output(unicode(translate.translate(seedStr,transInto,'en')),mihkel.robotName)
        
        c += 1
    print 'Limit reached, bye!'
    sys.exit(0)


# Don't want the text to get too long. This could probably be done better. Return only the 1st sentence. TO FIX: Missing punctuation!
# Will crash if sentence too short / missing unctuation
def shorten(str):
    markers = re.compile('[.!?]')
    tempStr = markers.split(str)
    return tempStr[1]


# Print output and write it to a logfile
def output(str,name, color = 0):
    random.seed()
    randomSleep = random.randint(1,3)
    
    wStr = unicode(str + '\n\n')
    if logFileName == '':
        pass
    else:
        f = open(logFileName,'a')
        f.write(name + ': ' + wStr.encode('UTF-8'))
        f.close
    
    if color:
        startColor = '\033[91m'
    else:
        startColor = '\033[92m'
    print startColor + name + ': \033[0m' + unicode(str)
    time.sleep(randomSleep)



if __name__ == '__main__':
    print 'Talky-AI Press Ctrl+C to exit. "./talky-AI.py --help" for more.'
    try:
        main()
    except KeyboardInterrupt:
        pass