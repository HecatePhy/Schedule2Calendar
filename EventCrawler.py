from Utils import *
import requests
from urllib.parse import urlparse
import os.path
from bs4 import BeautifulSoup

# TODO: html template lex

def parse_dodgers_2025_schedule(soup):
    event_list = []

    table_entries = soup.find_all('table')
    for entry in table_entries:
        month_num = None
        date_num = None
        hours_num = None
        minutes_num = None
        timezone = None
        is24 = None
        localtime = None
        eventtitle = None
        for div in entry.find_all('div'):
            if 'class' not in div.attrs.keys():
                continue
            if div['class'][0] == "month-date":
                month, date = div.string.split()
                month_num = month_brief2num[month]
                date_num = int(date)
            elif div['class'][0] == "primary-time":
                # TODO: update TBD things
                if len(div.string.split()) < 3:
                    hours_num = 5
                    minutes_num = 0
                    is24 = 2
                    timezone = 'PDT'
                else:
                    hours_num = int(div.string.split(':')[0])
                    minutes_num = int(div.string.split()[0].split(':')[1])
                    timezone = div.string.split()[-1]
                    is24 = 0
                    if div.string.split()[1] == 'am':
                        is24 = 1
                    elif div.string.split()[1] == 'pm':
                        is24 = 2
                localtime = transfer2localtime(timezone, 2025, month_num, date_num, hours_num, minutes_num, is24)
            elif div['class'][0] == "opponent-name":
                opname = div.string
                eventtitle = "MLB Dodgers vs %s" % opname
        event_list.append(["sportslive", eventtitle, localtime, 2])

    return event_list

def eventCrawler(link, pfunc):
    content_html = None
    if all([urlparse(link).scheme, urlparse(link).netloc]):
        try:
            response = requests.get(link)
        except requests.exceptions.RequestException as error:
            print(error)
            exit(1)
        content_html = response.content
    elif os.path.exists(link):
        with open(link, 'r', encoding='utf-8') as f:
            content_html = f.read()
    else:
        print("[ERROR] Not a url nor a filepath")
        exit(1)

    soup = BeautifulSoup(content_html, "html.parser")
    #print(soup.prettify())

    return pfunc(soup)
