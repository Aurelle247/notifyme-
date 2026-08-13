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
