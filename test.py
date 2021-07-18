#-*- coding: utf-8 -*-

import urllib.request
from bs4 import BeautifulSoup

def download_html(url):
    with urllib.request.urlopen(url) as response:
        html = response.read()
    return html

def scraper(url):
    html = download_html(url)
    soup = BeautifulSoup(html.decode('euc-kr', 'replace'), 'html.parser')

    title_links = soup.findAll('h1')
    articles = {}
    for link in title_links:
        if link.a:
            articles[link.a['href']] = link.text.strip()

    for article in articles:
        print(f'{articles[article]} - {article}')

if __name__ == '__main__':
    url = 'https://finance.naver.com/'
    scraper(url)
