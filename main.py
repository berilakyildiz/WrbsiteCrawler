import requests
from bs4 import BeautifulSoup



target_url = "https://uzem.adu.edu.tr"
foundLinks = []

def make_request(url):
    response = requests.get(target_url)
    soup = BeautifulSoup(response.text,"html.parser")
    return soup

def crawl(url):
    links = make_request(url)
    for link in links.find_all('a'):
        found_link = link.get('href')
        if "#" in found_link:
            found_link = found_link.split('#')[0]
        if target_url in found_link and found_link not in foundLinks:
            foundLinks.append(found_link)
            print(found_link)
            crawl(found_link)

crawl(target_url)



