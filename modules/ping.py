#!/usr/bin/env python
"""
ping.py - Torp Ping Module
Author: Sean B. Palmer, inamidst.com
About: http://inamidst.com/phenny/
"""

import random

def hello(torp, input): 
   greeting = random.choice(('Hi', 'Hey', 'Hello'))
   punctuation = random.choice(('', '!'))
   torp.say(greeting + ' ' + input.nick + punctuation)
hello.rule = r'(?i)(hi|hello|hey) $nickname\b'

def interjection(torp, input): 
   torp.say(input.nick + '!')
interjection.rule = r'$nickname!'
interjection.priority = 'high'
interjection.thread = False

if __name__ == '__main__': 
   print __doc__.strip()
