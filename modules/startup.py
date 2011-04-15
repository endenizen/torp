#!/usr/bin/env python
"""
startup.py - Torp Startup Module
Copyright 2008, Sean B. Palmer, inamidst.com
Licensed under the Eiffel Forum License 2.

http://inamidst.com/phenny/
"""

def startup(torp, input): 
   if hasattr(torp.config, 'serverpass'): 
      torp.write(('PASS', torp.config.serverpass))

   if hasattr(torp.config, 'password'): 
      torp.msg('NickServ', 'IDENTIFY %s' % torp.config.password)
      __import__('time').sleep(5)

   # Cf. http://swhack.com/logs/2005-12-05#T19-32-36
   for channel in torp.channels: 
      torp.write(('JOIN', channel))
startup.rule = r'(.*)'
startup.event = '251'
startup.priority = 'low'

if __name__ == '__main__': 
   print __doc__.strip()
