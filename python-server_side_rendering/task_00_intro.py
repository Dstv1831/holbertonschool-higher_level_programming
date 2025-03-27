import os

file_path='/DSTV/holbertonschool-higher_level_programming/python-server_side_rendering/template.txt'

# attendees = [
#     {"name": "Alice", "event_title": "Python Conference", "event_date": "2023-07-15", "event_location": "New York"},
#     {"name": "Bob", "event_title": "Data Science Workshop", "event_date": "2023-08-20", "event_location": "San Francisco"},
#     {"name": "Charlie", "event_title": "AI Summit", "event_date": None, "event_location": "Boston"}
# ]

# with open('template.txt', 'r') as file:
#     template_content = file.read()

# VERY IMPORTANT USE OF .ITEMS() .GET() AND ENUMERATE() ON DICTIONARIES

def generate_invitations (template, attendees):
    try:
        if not isinstance(template, str):
            raise TypeError("template must be a string")
        if not isinstance(attendees, list):
            raise TypeError("attendees must be a list")
        if not all(isinstance(items, dict) for items in attendees):
            raise TypeError("items on the attendees must be dictionaries")
        if not template:
            raise ValueError("Template is empty, no output files generated")
        if not attendees:
            raise ValueError("No data provided, no output files generated")
        for i, att in enumerate(attendees):
            new_template = template.replace("{name}", att.get('name', 'N/A'))\
                        .replace("{event_title}", att.get('event_title', 'N/A'))\
                        .replace("{event_date}", att.get('event_date', 'N/A'))\
                        .replace("{event_location}", att.get('event_location', 'N/A'))
            with open(f'output_{i}', 'w') as invitation:
                invitation.write(new_template)
    except (TypeError, ValueError) as e:
        print (f"Error: {e}")

    