import codecs
import socks, socket, time
from datetime import date
import urlparse
import httplib
import mechanize
import os, re
import subprocess
from bs4 import BeautifulSoup

counter = 1
httplib.HTTPConnection._http_vsn = 10
httplib.HTTPConnection._http_vsn_str = 'HTTP/1.0'
baseUrl = "https://en.wikipedia.org/wiki/Animal_Crossing:_New_Horizons"
socks.setdefaultproxy(socks.PROXY_TYPE_SOCKS5, '127.0.0.1', 9150)

