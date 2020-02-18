# Importing Required Labraries

from bs4 import BeautifulSoup as soup
import requests
import csv
import pandas as pd


# Parsing function
def func_html_parser(parse_url):
    url_request = requests.get(parse_url)
    page_soup = soup(url_request.content, 'html5lib')
    return page_soup


# csv write function 
def func_write_to_csv():
    'hi'

    
 # main function
def main():
    url = 'https://today.uci.edu/calendar'

    page_soup_content = func_html_parser(url)
    event_list = page_soup_content.findAll('div', attrs={'class': 'item_content_medium'})

    event_url_list = []
    for item in event_list:
        item_url = item.find('a')['href']
        event_url_list.append(item_url)

    for item_url in event_url_list:
        event_page_soup_content = func_html_parser(item_url)

        info = title = event_page_soup_content.find('div', attrs={'class': 'box_content vevent grid_8'})
        title = info.find('h1').text.strip()
        description = info.find('div', attrs={'class': 'description'}).text.strip()

        details = event_page_soup_content.find('div', attrs={'class': 'extra_details clearfix'})
        try:
            event_type = details.find('dd', attrs={'class': 'filter-event_types'}).text.strip()
            event_type_url = details.find('dd', attrs={'class': 'filter-event_types'}).find('a')['href']
        except Exception:
            event_type = 'N/A'
            event_type_url = 'N/A'
            pass
        try:
            Aduience = details.find('dd', attrs={'class': 'filter-event_audience'}).text.strip()
        except Exception:
            Aduience = 'N/A'
            pass
        website = details.find('dd', attrs={'class': 'event-website'}).find('a')['href']
        try:
            Department = details.find('dd', attrs={'class': 'event-group'}).find('a').text.strip()
            Department_url = details.find('dd', attrs={'class': 'event-group'}).find('a')['href']
        except Exception:
            Department = 'N/A'
            Department_url = 'N/A'
            pass

        try:
            HashTag = details.find('dd', attrs={'class': 'event-hashtag'}).find('a').text.strip()
            HashTag_url = details.find('dd', attrs={'class': 'event-hashtag'}).find('a')['href']
        except Exception:
            HashTag = 'N/A'
            HashTag_url = 'N/A'
            pass

        try:
            event_sponser = details.find('dd', attrs={'class': 'custom-field-event_sponsor'}).find('p').text.strip()
        except Exception:
            event_sponser = 'N/A'
            pass

        try:
            event_contact_email = details.find('dd', attrs={'class': 'custom-field-event_contact_email'}).find('a').text.strip()
        except Exception:
            event_contact_email = 'N/A'
            pass

        try:
            event_contact_phone = details.find('dd', attrs={'class': 'custom-field-event_contact_phone'}).find('p').text.strip()
        except Exception:
            event_contact_phone = 'N/A'
            pass

        event_date = ''
        event_time = ''
        venue = 'next page'
        venue_url = 'next page'
        try:
            addr = info.find('p', attrs={'class': 'location'})
            addr1 = addr.find('i').text.strip()
            addr2 = addr.find('span').text.strip()
            address = addr1 + ', ' + addr2
            try:
                address_url = addr.find('a')['href']
            except Exception:
                address_url = 'N/A'
                pass
        except Exception:
            address = 'N/A'
            pass

        Addmission_opening_timing = ''

        
  # test purpose
        print('title=  ' +title)
        print("description = "+description)
        print('event_type= '+event_type)
        print('event_type_url= '+event_type_url)
        print('Aduience= '+Aduience)
        print('Department= '+Department)
        print('Department_url= '+Department_url)
        print('HashTag= '+HashTag)
        print('HashTag_url= '+HashTag_url)
        print('event_sponser= '+event_sponser)
        print('event_contact_email= '+event_contact_email)
        print('event_contact_phone= '+event_contact_phone)
        print('address= '+address)
        print('address_url= '+address_url)

        print('-----------------')

if __name__ == '__main__':
    main()
