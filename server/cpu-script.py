#!/usr/bin/python2

# Kindle CPU Stat display
# Tim Bowers
# March 2019
#

template = 'weather-script-preprocess_wind.svg'

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

if temps_display:
   output = output.replace('HIGH_ONE',str(highs[0]))
   output = output.replace('HIGH_TWO',str(highs[1]))
   output = output.replace('HIGH_THREE',str(highs[2]))
   output = output.replace('HIGH_FOUR',str(highs[3]))
else:
   output = output.replace('WIND_ONE'  ,wind_icon[0])  
   output = output.replace('WIND_TWO'  ,wind_icon[1])  
   output = output.replace('WIND_THREE',wind_icon[2])  
   output = output.replace('WIND_FOUR' ,wind_icon[3])  
   output = output.replace('BFT_ONE'  ,speed_bft[0])
   output = output.replace('BFT_TWO'  ,speed_bft[1])
   output = output.replace('BFT_THREE',speed_bft[2])
   output = output.replace('BFT_FOUR' ,speed_bft[3])

   

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
