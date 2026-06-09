import requests

# TODO: Get price information (Trading post).
# TODO: Allow for names to be entered to get information.
# TODO: Allow for repeated attempts after an invalid input.

# Input
item = input("Enter the ID of the item you are looking for: ")

# Validate
if not item.isdigit():
    print("Please enter a numeric item ID.")

else:
    # Using requests.get to get the input item's information using ID
    response = requests.get(f"https://api.guildwars2.com/v2/items/{item}")
    data = response.json()

    if response.status_code == 200:
        print(data["name"])
    
    else:
        print("Could not find that item.")
        print("API message:", data.get("text", "Unknown error"))
