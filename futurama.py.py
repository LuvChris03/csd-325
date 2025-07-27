futurama.py
import requests
import json

# Base API URL (public Futurama API endpoint)
BASE_URL = "https://futurama-api.fly.dev/"

# List of characters to test
CHARACTERS = [
    "Bender", "Fry", "Leela", "Professor Farnsworth", "Amy",
    "Zapp Brannigan", "Lurr", "Dr Zoidberg", "Linda the reporter",
    "Bob Barker", "Hermes", "Morgan Proctor", "Mom",
    "Robot Mob", "Giant Bender", "Kif", "Don bot"
]

# Convert character name to API-friendly format
def format_name_for_api(name):
    return name.lower().replace(" ", "-")

# Fetch data from API
def fetch_character_data(name):
    formatted_name = format_name_for_api(name)
    url = BASE_URL + formatted_name
    response = requests.get(url)

    if response.status_code == 200:
        return response.json()
    else:
        return None

# Print raw JSON response
def print_raw_response(response):
    print("Raw Response:")
    print(response)

# Print formatted JSON response
def print_formatted_response(response):
    print("\nFormatted Response:")
    print(json.dumps(response, indent=4))

# Display single character nicely
def display_character(character):
    if character:
        print(f"\nCharacter: {character[0]['character']}")
        print(f"Image URL: {character[0]['image']}")
        print(f"Quote: {character[0]['quote']}")
    else:
        print("Character not found or no data available.")

# Main program
def main():
    # Show raw + formatted data for first character (Bender) as tutorial example
    first_char = fetch_character_data("Bender")
    print_raw_response(first_char)
    print_formatted_response(first_char)

    # Interactive search
    while True:
        print("\n--- Futurama Character Search ---")
        print("Type a character name (e.g., 'Zapp Brannigan'), 'list' to view all, or 'quit' to exit.")
        choice = input("Enter choice: ").strip()

        if choice.lower() == "quit":
            break
        elif choice.lower() == "list":
            print("\nAvailable Characters:")
            for name in CHARACTERS:
                print(f" - {name}")
        else:
            character_data = fetch_character_data(choice)
            display_character(character_data)

if __name__ == "__main__":
    main()
