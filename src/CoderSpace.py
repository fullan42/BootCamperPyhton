import requests
from bs4 import BeautifulSoup as bs

class CoderspaceEventDataAdvanced:
    def __init__(self, url):
        self.url = url
        self.data = []

    def scrape_data(self):
        headers = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
        }
        page = requests.get(self.url, headers=headers)
        soup = bs(page.content, 'html.parser')

        events = soup.find_all('div', {'class': 'event-card'})

        for item in events:
            event_info = {}

            name = item.find('h5').text.strip()
            event_info['name'] = name

            link = item.find('h5').find('a')['href']
            event_info['link'] = "https://coderspace.io/"+link

            description = item.find('p').text.strip()
            event_info['description'] = description

            ahrefForImages = item.find('a', {'class': 'event-card-image'})

            img_tag = ahrefForImages.find('img')

            img_src = img_tag['src']
            event_info['image_src'] = img_src

            eventType = item.find('span', {'class': 'event-card-type'}).text.strip()
            event_info['eventType'] = eventType

            deadline = item.find('ul', {'class': 'event-card-info'}).find('strong').text.strip()
            event_info['deadline'] = deadline

            application_status = item.find('a', {'class': 'primary-button'})
            if application_status:
                status_text = application_status.find('span').text.strip()
                event_info['application_status'] = status_text

            self.data.append(event_info)

    def get_event_data(self):
        return self.data
