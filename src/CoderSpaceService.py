class CoderspaceService:
    def __init__(self, data):
        self.events = []
        for item in data:
            event_info = {
                "name": item['name'],
                "img_src": item['image_src'],  # Updated key to 'image_src'
                "link": item['link'],
                "description": item['description'],
                "eventType": item['eventType'],
                "deadline": item['deadline']
            }

            if 'application_status' in item:
                event_info['application_status'] = item['application_status']

            self.events.append(event_info)

    def as_list(self):
        return self.events
