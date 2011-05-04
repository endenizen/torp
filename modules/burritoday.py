import web, re

loc = re.compile(r'center=([0-9\.]+),(-[0-9\.]+)&')
pretty_name = re.compile(r'<span class="geocode">(.*?)<\/span>')
recency = re.compile(r'<span class="location_badge_duration">(.*?)<\/span>')

def burritoloc(torp, input):
  uri = 'http://www.google.com/latitude/apps/badge/api?user=797967215506697296&type=iframe&maptype=roadmap'
  bytes = web.get(uri)
  (lat,lng) = loc.findall(bytes)[0]
  name = pretty_name.findall(bytes)[0]
  ago = recency.findall(bytes)[0]
  torp.say(name + ' (' + lat + ',' + lng + ') ' + ago)
burritoloc.commands = ['burritos']
burritoloc.example = ['burritos']

if __name__ == '__main__':
  print __doc__.strip()
