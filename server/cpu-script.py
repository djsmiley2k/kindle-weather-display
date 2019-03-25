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

output = output.replace('CPU_V',str(cpu_temp))
output = output.replace('NB_V',str(nb_temp))
output = output.replace('HDD_V',str(hdd_temp))
output = output.replace('LOAD_V',str(load))
output = output.replace('UPTIME_V',str(uptime))

# Insert current time
# (thanks Jennifer http://www.shatteredhaven.com/2012/11/1347365-kindle-weather-display.html)
output = output.replace('DATE_VALPLACE',str(dtnow))

# Write output
codecs.open('cpu-script-output.svg', 'w', encoding='utf-8').write(output)

# EOF
