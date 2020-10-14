import urllib
import time
import datetime
import json

url="http://api.openweathermap.org/data/2.5/weather?q=canada%20de%20gomez&units=imperial&appid=10b47b3e0e224c8fbd6d02673886f75a"
wxfile = "C:\\Weather\\zara.html"
a = "C:\\Weather\\a.html"
response = urllib.urlopen(url)

data = json.loads(response.read())
temp_f = data['main']['temp']
humidity = data['main']['humidity']

linesout = []
linesout.append('<HTML>')
linesout.append('Temperature: '+str(temp_f)+'<BR/>')
linesout.append('Humidity: '+str(humidity)+'<BR/>')
linesout.append('</HTML>')


f = open(wxfile,'w')
f.write("\n".join(linesout))
f.close()