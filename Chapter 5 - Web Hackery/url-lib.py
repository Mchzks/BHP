import urllib.parse
import urllib.request

# GET Request
url = 'http://google.com'
with urllib.request.urlopen(url) as response:
    content = response.read()

print(content)

# POST Request
info = {'user': 'tim', 'passwd':'31337'}
data = urllib.parse.urlencode(info).encode()

req = urllib.request.Request(url, data)
with urllib.request.urlopen(req) as response:
    content = response.read()

print(content)

# Request Library
import requests
url = 'http://boodelyboo.com'
response = requests.get(url)

info = {'user': 'tim', 'passwd':'31337'}
response = requests.get(url, data=data)

print(response.text)

# lxml and BeutifukSoup Packages
# pip install lxml
from io import BytesIO
from lxml import etree
import requests

url = 'http://nostarch.com'
r = requests.get(url)
content = r.content

parser = etree.HTMLParser()
content = etree.parse(BytesIO(content), parser=parser)
for link in content.findall('//a'):
    print(f"{link.get('href')} -> {link.text}")

# pip install beutifulsoup4
from bs4 import BeautifulSoup as bs
import requests

url = 'http://bing.com'
r = requests.get(url)

tree = bs(r.text, 'html.parser')
for link in tree.find_all('a'):
    print(f"{link.get('href')} -> {link.text}")
