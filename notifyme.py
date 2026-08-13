#import requests
#import os
#site = input("Enter site url or filepath: ")
#site_content = ""
#try:
#   if site.startswith("http://") or site.startswith("https://"):
#      response = requests.get(site)
#      response.encoding = 'utf-8'
#      site_content = response.text
#   else:
#      with open(site, "r", encoding="utf-8") as file:
#         site_content = file.read()
#   print("Read", len(site_content), "characters.")
#except FileNotFoundError:
#   print("file not found.")
#except requests.exceptions.RequestException as e:
#   print("Error fetching the site:", e)


#message = input("Enter notification message: ")

#f len(site_content) >+ 10:
#   print(message)

import requests
import time
import os

def get_content(source):
    """Return content from a URL or local file."""
    if source.startswith("http://") or source.startswith("https://"):
        try:
            response = requests.get(source)
            response.encoding = "utf-8"
            return response.text
        except requests.exceptions.RequestException as e:
            print("Error fetching URL:", e)
            return ""
    else:
        try:
            with open(source, "r", encoding="utf-8") as file:
                return file.read()
        except FileNotFoundError:
            print("File not found.")
            return ""

# --- Main program ---
site = input("Enter site URL or filepath: ")
message = input("Enter notification message: ")

print("Monitoring started... Press Ctrl+C to stop.")

# Get initial content
previous_content = get_content(site)

while True:
    time.sleep(10)  # check every 10 seconds (adjust as needed)
    current_content = get_content(site)

    if current_content and current_content != previous_content:
        print("Change detected!")
        print(message)
        previous_content = current_content
