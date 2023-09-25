import csv
import os
import json
import random
import string

# Define the input CSV file and the output folder (1)
csv_file = 'mybookmarks.csv'
output_folder = 'D:\path\to\your\eagle\library\images'

# Create the output folder if it doesn't exist
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Function to generate a random folder name (13 characters)
def generate_random_folder_name():
    folder_name = ''.join(random.choices(string.ascii_uppercase + string.digits, k=13))
    return folder_name

# Function to create metadata JSON (2)
def create_metadata_json(title, tags, url, folder_name):
    metadata = {
        "name": title,
        "ext": "url",
        "tags": [tags],
        "url": url,
        "folders": ["LM9LXUDKPIJF4"],
        "id": folder_name
    }
    return metadata

# Read the CSV file
with open(csv_file, 'r', newline='', encoding='utf-8') as csvfile:
    reader = csv.reader(csvfile)
    next(reader)  # Skip the header row
    for row in reader:
        url = row[0].strip()
        title = row[1].strip()
        tags = row[2].strip()

        # Generate a random folder name
        folder_name = generate_random_folder_name()

        # Create a folder with the .info extension
        pair_folder = os.path.join(output_folder, f"{folder_name}.info")
        os.makedirs(pair_folder, exist_ok=True)

        # Create .url file inside the pair folder
        url_filename = os.path.join(pair_folder, f"{title}.url")
        with open(url_filename, 'w', encoding='utf-8') as url_file:
            url_file.write('[InternetShortcut]\n')
            url_file.write('URL=' + url)

        # Create metadata JSON file (always named "metadata.json") inside the pair folder
        metadata = create_metadata_json(title, tags, url, folder_name)
        metadata_filename = os.path.join(pair_folder, "metadata.json")
        with open(metadata_filename, 'w', encoding='utf-8') as metadata_file:
            json.dump(metadata, metadata_file, indent=4)

print("Import completed.")
