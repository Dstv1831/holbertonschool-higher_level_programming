import os

attendees = [
    {"name": "Alice", "event_title": "Python Conference", "event_date": "2023-07-15", "event_location": "New York"},
    {"name": "Bob", "event_title": "Data Science Workshop", "event_date": "2023-08-20", "event_location": "San Francisco"},
    {"name": "Charlie", "event_title": "AI Summit", "event_date": None, "event_location": "Boston"}
]

with open('template.txt', 'r') as file:
    template_content = file.read()

# VERY IMPORTANT USE OF .ITEMS() .GET() AND ENUMERATE() ON DICTIONARIES

def generate_invitations(template, attendees):
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
            new_template = template.replace("{name}", str(att.get('name', 'N/A')))\
                        .replace("{event_title}", str(att.get('event_title', 'N/A')))\
                        .replace("{event_date}", str(att.get('event_date', 'N/A')))\
                        .replace("{event_location}", str(att.get('event_location', 'N/A')))
            
            file_name = f'output_{i}.txt'
            if os.path.exists(file_name):
                print(f"Skipping {file_name}, alredy exist")
                continue
            else:
                with open(file_name, 'w') as invitation:
                    invitation.write(new_template)
    except (TypeError, ValueError) as e:
        print (f"Error: {e}")

generate_invitations(template_content, attendees)