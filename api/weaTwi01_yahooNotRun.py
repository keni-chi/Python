# -*- coding: utf-8 -*-
import pywapi
import string

yahoo_result = pywapi.get_weather_from_yahoo('10001')
print "Yahoo says: It is " + string.lower(yahoo_result['condition']['text']) + " and " + yahoo_result['condition']['temp'] + "C now in New York.\n\n"


result = pywapi.get_weather_from_yahoo('JAXX0085')

'''
print("001")
astronomy = result['astronomy']
condition = result['condition']['text']
print "Current Tokyo Weather: " + condition
'''


'''
weather = '---\n' + \
    result['title'] + '\n現在の' + \
    result['location']['city'] + u'の天気:' + \
    result['condition']['text'] + u'\n' +\
    u'---'

print weather
'''
