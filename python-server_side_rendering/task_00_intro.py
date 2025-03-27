import os

file_path='/DSTV/holbertonschool-higher_level_programming/python-server_side_rendering/template.txt'

attendees = [
    {"name": "Alice", "event_title": "Python Conference", "event_date": "2023-07-15", "event_location": "New York"},
    {"name": "Bob", "event_title": "Data Science Workshop", "event_date": "2023-08-20", "event_location": "San Francisco"},
    {"name": "Charlie", "event_title": "AI Summit", "event_date": None, "event_location": "Boston"}
]

with open('template.txt', 'r') as file:
    template_content = file.read()

def generate_invitations (template, attendees):
    if isinstance(template, str) or isinstance(attendees, list):
        if template and attendees:
            for att in attendees:
                template.replace("{name}", att['name'])
                template.replace("{event_title}", att['event_title'])
                template.replace("{event_date}", att['event_date'])
                template.replace("{event_location}", att['event_location'])
                with open(f'output_{attendees.index(att)}', 'w') as invitation:
                    invitation.write(template)
        else:
            raise Exception("Either template or attendees are empty")
    else:
        TypeError("template must be a String and attendees must be a List")
        return
    
generate_invitations(template_content, attendees)
