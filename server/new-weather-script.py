#!/usr/bin/python

# Kindle Weather Display
# Matthew Petroff (http://www.mpetroff.net/)
# September 2012
#
# Owen Bullock - UK Weather - MetOffice - Aug 2013
#
#

import urllib2
from xml.dom import minidom
import datetime
import codecs


#
# MetOffice API Key
#
myApiKey="7557844e-c57a-4fc6-90d0-055fcce3018c"




#
#  magic Svg template
#
template = 'weather-script-preprocess_temps.svg'

#
#  Map the MetOffice weather codes to Icons. 
# ( See http://www.metoffice.gov.uk/datapoint/product/uk-3hourly-site-specific-forecast )
#
mapping = [ 
[0 , 'skc     '],  #  Clear night                     skc.svg
[1 , 'skc     '],  #  Sunny day                       skc.svg
[2 , 'sct     '],  #  Partly cloudy (night)           sct.svg
[3 , 'sct     '],  #  Partly cloudy (day)             sct.svg
[4 , '        '],  #  Not used                        -
[5 , 'fg      '],  #  Mist                            fg.svg
[6 , 'fg      '],  #  Fog                             fg.svg
[7 , 'bkn     '],  #  Cloudy                          bkn.svg
[8 , 'ovc     '],  #  Overcast                        ovc.svg
[9 , 'hi_shwrs'],  #  Light rain shower (night)       hi_shwrs.svg
[10, 'hi_shwrs'],  #  Light rain shower (day)         hi_shwrs.svg
[11, 'hi_shwrs'],  #  Drizzle                         hi_shwrs.svg
[12, 'ra1     '],  #  Light rain                      ra1.svg
[13, 'ra      '],  #  Heavy rain shower (night)       ra.svg
[14, 'ra      '],  #  Heavy rain shower (day)         ra.svg
[15, 'ra      '],  #  Heavy rain                      ra.svg
[16, 'rasn    '],  #  Sleet shower (night)            rasn.svg
[17, 'rasn    '],  #  Sleet shower (day)              rasn.svg
[18, 'rasn    '],  #  Sleet                           rasn.svg
[19, 'ip      '],  #  Hail shower (night)             ip.svg
[20, 'ip      '],  #  Hail shower (day)               ip.svg
[21, 'ip      '],  #  Hail                            ip.svg
[22, 'sn      '],  #  Light snow shower (night)       sn.svg
[23, 'sn      '],  #  Light snow shower (day)         sn.svg
[24, 'sn      '],  #  Light snow                      sn.svg
[25, 'sn      '],  #  Heavy snow shower (night)       sn.xvg
[26, 'sn      '],  #  Heavy snow shower (day)         sn.svg
[27, 'sn      '],  #  Heavy snow                      sn.svg
[28, 'tsra    '],  #  Thunder shower (night)          tsra.svg
[29, 'tsra    '],  #  Thunder shower (day)            tsra.svg
[30, 'tsra    '],  #  Thunder                         tsra.svg
]



#
# Download and parse weather data - location 352448 = Loughton, Essex
#
url='http://datapoint.metoffice.gov.uk/public/data/val/wxfcs/all/xml/352448?res=daily&key='+myApiKey
weather_xml = urllib2.urlopen(url).read()
dom = minidom.parseString(weather_xml)



# get date
periods=dom.getElementsByTagName('Period')
today_str = periods[0].getAttribute('value')
today_dt= datetime.datetime.strptime(today_str, '%Y-%m-%dZ')
print "DAY:",today_dt


dtnow=datetime.datetime.now().strftime("%d-%b %H:%M")
print "NOW:",dtnow

# get temps:  Dm is Day Max, FDm is Feels Like Day Max
# get weather: W is weather type
highs = [None]*7
feels = [None]*7
icons =  [None]*7
i=0;

for period in periods:
    thisDay=period.getAttribute('value')
    print "period:",i
    Reps = period.getElementsByTagName('Rep')
       # temps
    highs[i] = Reps[0].getAttribute('Dm')  # 0 = Day 1= Night
    feels[i] = Reps[0].getAttribute('FDm')
    print "   DayMax:",highs[i]
    print "   Feels :",feels[i]
       # weather 
    weather= int(Reps[0].getAttribute('W'))
    icons[i] = mapping[weather][1];
    icons[i] = icons[i].rstrip(' ')
    print "      Weather :",weather,icons[i]+'.svg'
      # and loop
    i=i+1
     


	




#
# Preprocess SVG
#

# Open SVG to process
output = codecs.open(template , 'r', encoding='utf-8').read()

# Insert weather icons and temperatures
output = output.replace('ICON_ONE',icons[0])
output = output.replace('ICON_TWO',icons[1])
output = output.replace('ICON_THREE',icons[2])
output = output.replace('ICON_FOUR',icons[3])

output = output.replace('HIGH_ONE',str(highs[0]))
output = output.replace('HIGH_TWO',str(highs[1]))
output = output.replace('HIGH_THREE',str(highs[2]))
output = output.replace('HIGH_FOUR',str(highs[3]))

output = output.replace('LOW_ONE',str(feels[0]))
output = output.replace('LOW_TWO',str(feels[1]))
output = output.replace('LOW_THREE',str(feels[2]))
output = output.replace('LOW_FOUR',str(feels[3]))

# Insert current time 
# (thanks Jennifer http://www.shatteredhaven.com/2012/11/1347365-kindle-weather-display.html)
output = output.replace('DATE_VALPLACE',str(dtnow))

# Insert days of week
one_day = datetime.timedelta(days=1)
print " ONE DAY:",one_day

days_of_week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
print days_of_week[(today_dt + 2*one_day).weekday()]
print days_of_week[(today_dt + 3*one_day).weekday()]

output = output.replace('DAY_THREE',days_of_week[(today_dt + 2*one_day).weekday()])
output = output.replace('DAY_FOUR',days_of_week[(today_dt + 3*one_day).weekday()])

# Write output
codecs.open('weather-script-output.svg', 'w', encoding='utf-8').write(output)

# EOF
