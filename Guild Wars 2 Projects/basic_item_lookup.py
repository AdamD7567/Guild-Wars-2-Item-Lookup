import requests

# Input
item = input("Enter the ID of the item you are looking for: ")

# Using requests.get to get the input item's information using ID
response = requests.get(f"https://api.guildwars2.com/v2/items/{item}")
data = response.json()

# Making sure we get a safe return for debugging purposes.
if response.status_code == 200:
    data = response.json()
    print(data["name"])

else:
    print("Something went wrong.")
    print("Status code:", response.status_code)
    print(response.text)