import requests
from bs4 import BeautifulSoup as bs

class TechCareerData:
    def __init__(self, url):
        self.url = url
        self.names = []
        self.img_urls = []
        self.dates = []

    def scrape_data(self):
        baslik = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
        }
        page = requests.get(self.url, headers=baslik)
        soup = bs(page.content, 'html.parser')

        Names = soup.find_all('h3', {'class': 'MuiTypography-root MuiTypography-h6 css-r0m1bi'})
        imgUrl = soup.find_all('img', {'data-test': 'single-event-image'})
        dates = soup.find_all('div', {'class': 'MuiTypography-root MuiTypography-subtitle2 css-l8rqx2'})

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

    def get_combined_data(self):
        return list(zip(self.names, self.img_urls, self.dates))

# Kullanımı
tech_career = TechCareerData('https://www.techcareer.net/bootcamp')
tech_career.scrape_data()
combined_data = tech_career.get_combined_data()

