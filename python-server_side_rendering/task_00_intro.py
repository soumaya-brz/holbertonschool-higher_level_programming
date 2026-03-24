# task_00_intro.py

import os

def generate_invitations(template, attendees):
    # Vérifier les types
    if not isinstance(template, str):
        print(f"Error: template must be a string, got {type(template).__name__}")
        return
    if not isinstance(attendees, list) or not all(isinstance(a, dict) for a in attendees):
        print(f"Error: attendees must be a list of dictionaries, got {type(attendees).__name__}")
        return

    # Vérifier les entrées vides
    if not template.strip():
        print("Template is empty, no output files generated.")
        return
    if not attendees:
        print("No data provided, no output files generated.")
        return

    # Parcourir chaque attendee
    for index, attendee in enumerate(attendees, start=1):
        # Créer une copie du template
        content = template
        # Remplacer chaque placeholder
        for placeholder in ['name', 'event_title', 'event_date', 'event_location']:
            value = attendee.get(placeholder)
            if not value:
                value = "N/A"
            content = content.replace(f"{{{placeholder}}}", value)

        # Nom du fichier de sortie
        filename = f"output_{index}.txt"
        try:
            with open(filename, 'w') as f:
                f.write(content)
        except Exception as e:
            print(f"Error writing file {filename}: {e}")
