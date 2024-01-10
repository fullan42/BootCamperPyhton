class PatikaService:
    def __init__(self, combined_data):
        self.bootcamps = []
        for data in combined_data:
            bootcamp = {
                "link": data[0],
                "name": data[1],
                "img_url": data[2],
                "date": data[3],
                "place": data[4]
            }
            self.bootcamps.append(bootcamp)

    def as_list(self):
        return self.bootcamps
