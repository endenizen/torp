#!/usr/bin/env python
"""
info.py - Torp Information Module
Copyright 2008, Sean B. Palmer, inamidst.com
Licensed under the Eiffel Forum License 2.

http://inamidst.com/phenny/
"""

def doc(torp, input): 
   """Shows a command's documentation, and possibly an example."""
   name = input.group(1)
   name = name.lower()

   if torp.doc.has_key(name): 
      torp.reply(torp.doc[name][0])
      if torp.doc[name][1]: 
         torp.say('e.g. ' + torp.doc[name][1])
doc.rule = ('$nick', '(?i)(?:help|doc) +([A-Za-z]+)(?:\?+)?$')
doc.example = '$nickname: doc tell?'
doc.priority = 'low'

def commands(torp, input): 
   # This function only works in private message
   if input.sender.startswith('#'): return
   names = ', '.join(sorted(torp.doc.iterkeys()))
   torp.say('Commands I recognise: ' + names + '.')
   torp.say(("For help, do '%s: help example?' where example is the " + 
               "name of the command you want help for.") % torp.nick)
commands.commands = ['commands']
commands.priority = 'low'

def help(torp, input): 
   response = (
      'Hi, I\'m a bot. Say ".commands" to me in private for a list ' + 
      'of my commands, or see http://inamidst.com/phenny/ for more ' + 
      'general details. My owner is %s.'
   ) % torp.config.owner
   torp.reply(response)
help.rule = ('$nick', r'(?i)help(?:[?!]+)?$')
help.priority = 'low'

def stats(torp, input): 
   """Show information on command usage patterns."""
   commands = {}
   users = {}
   channels = {}

   ignore = set(['f_note', 'startup', 'message', 'noteuri'])
   for (name, user), count in torp.stats.items(): 
      if name in ignore: continue
      if not user: continue

      if not user.startswith('#'): 
         try: users[user] += count
         except KeyError: users[user] = count
      else: 
         try: commands[name] += count
         except KeyError: commands[name] = count

         try: channels[user] += count
         except KeyError: channels[user] = count

   comrank = sorted([(b, a) for (a, b) in commands.iteritems()], reverse=True)
   userank = sorted([(b, a) for (a, b) in users.iteritems()], reverse=True)
   charank = sorted([(b, a) for (a, b) in channels.iteritems()], reverse=True)

   # most heavily used commands
   creply = 'most used commands: '
   for count, command in comrank[:10]: 
      creply += '%s (%s), ' % (command, count)
   torp.say(creply.rstrip(', '))

   # most heavy users
   reply = 'power users: '
   for count, user in userank[:10]: 
      reply += '%s (%s), ' % (user, count)
   torp.say(reply.rstrip(', '))

   # most heavy channels
   chreply = 'power channels: '
   for count, channel in charank[:3]: 
      chreply += '%s (%s), ' % (channel, count)
   torp.say(chreply.rstrip(', '))
stats.commands = ['stats']
stats.priority = 'low'

if __name__ == '__main__': 
   print __doc__.strip()
