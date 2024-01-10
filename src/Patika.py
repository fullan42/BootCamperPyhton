import requests
from bs4 import BeautifulSoup as bs

class PatikaDevData:
    def __init__(self, url):
        self.url = url
        self.link = []
        self.names = []
        self.img_urls = []
        self.dates = []
        self.places = []

    def scrape_data(self):
        headers = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
        }
        page = requests.get(self.url, headers=headers)
        soup = bs(page.content, 'html.parser')

        a_tags = soup.find_all('a', {'class': 'link-block w-inline-block'})

        for a_tag in a_tags:
            href = a_tag.get('href')
            self.link.append(href)
            self.names.append(a_tag.find('h2').text)
            self.img_urls.append(a_tag.find('img').get('src'))
            self.dates.append(a_tag.find_next('div', {'class': 'bootcamp-dates'}).text)
            place_text = a_tag.find_next('div', {'class': 'location-details'}).text.strip().replace('\xa0', '')
            self.places.append(place_text)

    def get_combined_data(self):
        combined_data = []
        for i in range(len(self.link)):
            bootcamp_info = [
                self.link[i],
                self.names[i],
                self.img_urls[i],
                self.dates[i],
                self.places[i]
            ]
            combined_data.append(bootcamp_info)
        return combined_data

# Kullanımı
patika_data = PatikaDevData('https://www.patika.dev/programs')
patika_data.scrape_data()
combined_data = patika_data.get_combined_data()


