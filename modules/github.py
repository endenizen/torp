import web

def gitrepo(torp, input):
  q = input.group(2)
  uri = 'http://github.com/api/v2/json/repos/show/%s' % q
  bytes = web.get(uri)
  result = web.json(bytes)
  print result
  if result.has_key('error'):
    torp.say(result['error'])
  elif result.has_key('repository'):
    repo = result['repository']
    msg = '%s: %s. (%dw, %df) %s' % (repo['name'], repo['description'], repo['watchers'], repo['forks'], repo['url'])
    print msg
    torp.say(msg)
gitrepo.commands = ['repo']
gitrepo.example = '.repo endenizen/torp'

if __name__ == '__main__':
  print __doc__.strip()
