class CoderspaceService:
    def __init__(self, data):
        self.events = []
        for item in data:
            event_info = {
                "title": item['title'],
                "title_link": item['title_link'],
                "description": item['description'],
                "event_type": item['event_type'],
                "deadline": item['deadline']
            }

            if 'application_status' in item:
                event_info['application_status'] = item['application_status']

            self.events.append(event_info)

    def as_list(self):
        return self.events
