import requests
from bs4 import BeautifulSoup as bs

import requests

import requests
from bs4 import BeautifulSoup as bs

class TechCareerData:
    def __init__(self, url):
        self.url = url
        self.names = []
        self.img_urls = []
        self.link = []
        self.dates = []
        self.headers = {
            'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Mobile Safari/537.36'
        }
        self.page = None
        self.soup = None

    def scrape_data(self):
        self.page = requests.get(self.url, headers=self.headers)
        self.soup = bs(self.page.content, 'html.parser')
        # Veri çekme işlemlerini burada devam ettirebilirsiniz.

        links = self.soup.find_all('a', {'class': 'MuiTypography-root MuiTypography-inherit MuiLink-root MuiLink-underlineNone css-adfut0'})
        Names = self.soup.find_all('h3', {'class': 'MuiTypography-root MuiTypography-h6 css-r0m1bi'})
        imgUrl = self.soup.find_all('img', {'data-test': 'single-event-image'})
        dates = self.soup.find_all('div', {'class': 'MuiBox-root css-9s7nl0'})

        for button_etiketi in Names:
            button_icerik = button_etiketi.text
            self.names.append(button_icerik)

        for img_etiketi in imgUrl:
            img_url = img_etiketi.get('src')
            self.img_urls.append("https://www.techcareer.net/" + img_url)


        for tarih in dates:
            hepsi_icerik = tarih.text
            if "Başvurular Tamamlandı" not in hepsi_icerik:
                self.dates.append(hepsi_icerik)


        for link in links:
            link_href = link.get('href')
            self.link.append("https://www.techcareer.net/"+link_href)

    def get_combined_data(self):
        return list(zip(self.names, self.img_urls, self.dates, self.link))



