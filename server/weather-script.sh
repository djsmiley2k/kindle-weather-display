#!/bin/sh

cd "$(dirname "$0")"


date

echo "------ python get data from metoffice"
python2 new-weather-script.py

echo "------ convert to png"
convert -depth 8 -flatten weather-script-output.svg weather-script-output.png

echo "------ shrink png"
pngcrush -q -c 2 weather-script-output.png weather-script-output_s.png

echo "------ copy to webserver"
cp -f weather-script-output_s.png /var/www/localhost/htdocs/weather/weather-script-output.png
