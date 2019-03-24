#!/usr/bin/python2

# Kindle CPU Stat display
# Tim Bowers
# March 2019
#

template = 'cpu-script-preprocess.svg'

#
# Preprocess SVG
#

# Open SVG to process
output = codecs.open(template , 'r', encoding='utf-8').read()

# Insert values into SVG
output = output.replace('ICON_ONE',icons[0])
output = output.replace('ICON_TWO',icons[1])
output = output.replace('ICON_THREE',icons[2])
output = output.replace('ICON_FOUR',icons[3])

# Insert current time
# (thanks Jennifer http://www.shatteredhaven.com/2012/11/1347365-kindle-weather-display.html)
output = output.replace('DATE_VALPLACE',str(dtnow))

# Write output
codecs.open('weather-script-output.svg', 'w', encoding='utf-8').write(output)

# EOF
