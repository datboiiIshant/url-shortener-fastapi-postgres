# Simple Python Program built to shorten urls using the pyshorteners library in Python

import pyshorteners
s = pyshorteners.Shortener()

def convert(url):
    shortened_url = s.tinyurl.short(url) # shortens the URL using pyshorteners Library
    return {
        'url': url,
        'shortened_url': shortened_url
    }
# return a dictionary of result.

# convert('https://www.youtube.com/watch?v=398DuQbQJq0')