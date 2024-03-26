import requests
from bs4 import BeautifulSoup
import urllib.parse

def crawl_website(url):
  response = requests.get(url)
  soup = BeautifulSoup(response.content, "html.parser")
  return soup.prettify()

def get_filename(url):
  parsed_url = urllib.parse.urlparse(url)
  return parsed_url.netloc + ".html"
urls = [
  "https://cmlabs.co",
  "https://sequence.day",
  "https://kompas.com/"
]

for url in urls:
  filename = get_filename(url)
  html_content = crawl_website(url)
  with open(filename, "w", encoding="utf-8") as f:
    f.write(html_content)

print("Crawling selesai!")
