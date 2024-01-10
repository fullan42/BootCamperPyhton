from src.TechCareer import TechCareerData


class TechCareerService:
    def __init__(self, combined_data):
        self.bootcamps = []
        for data in combined_data:
            bootcamp = {
                "name": data[0],
                "img_url": data[1],
                "date": data[2],
                "link": data[3]
            }
            self.bootcamps.append(bootcamp)

    def as_list(self):
        return self.bootcamps

tech_career = TechCareerData('https://www.techcareer.net/bootcamp')
tech_career.scrape_data()
combined_data = tech_career.get_combined_data()

tech_service = TechCareerService(combined_data)
data_list = tech_service.as_list()


