# Guild Wars 2 Item Lookup

A small Python command-line project that uses the Guild Wars 2 API to look up item information and Trading Post prices.

I started this project as a personal Python refresher. I wanted to rebuild confidence with Python while working on something fun, practical, and that I'd actually use myself. The project focuses on using an external API, reading JSON responses, handling user input, and formatting useful output for the user.

## Features

* Look up a Guild Wars 2 item by item ID
* Search previously looked-up items by name using a local JSON cache
* Automatically save looked-up item IDs and names locally for future searches
* Display item information, including:

  * Name
  * Type
  * Rarity
  * Level
* Fetch & Display Trading Post price information, including:

  * Buy price
  * Sell price
  * Buy/sell spread
* Format prices into gold, silver, and copper
* Allow repeated searches without restarting the program
* Allow users to press Enter to skip cached name search and search by ID instead
* Validate user input before making API requests
* Handle basic API/network errors using try/except

## Example Output

```text
Enter the ID of the item you are looking for: 19721

Item information
--------------------
Name: Glob of Ectoplasm
Type: Trophy
Rarity: Exotic
Level: 0

Trading Post Information
--------------------
Buy price: 23s 10c
Sell price: 24s 55c
Spread: 1s 45c
```

## What I Learned

This project helped me practise several important Python and software development concepts:

* Making HTTP requests using the `requests` library
* Working with an external API
* Reading and using JSON data
* Accessing nested JSON values
* Reading from and writing to local JSON files
* Preventing duplicate entries in local JSON cache
* Using functions to organise code
* Using loops for repeated user interaction
* Validating user input
* Formatting raw API data into readable output
* Handling API/network errors using try/except
* Writing basic unit tests with pytest
* Building a small project incrementally using TODOs

One useful concept I learned was how to work with nested JSON. For example, Trading Post price data is returned as separate buy and sell sections when making the request, so the program needs to access nested values rather than assuming all data is at the top level.

## How to Run

1. Clone the repository:

```bash
git clone https://github.com/AdamD7567/Guild-Wars-2-Item-Lookup.git
```

2. Navigate into the project folder:

```bash
cd Guild-Wars-2-Item-Lookup
```

3. Install the required dependency:

```bash
pip install -r requirements.txt
```

4. Run the program:

```bash
python basic_item_lookup.py
```

## Running Tests

This project uses pytest for basic unit tests.

To run the tests:

```bash
python -m pytest
```


## Current Limitations

* Full Guild Wars 2 item-name search is not implemented yet.
* Name search currently only works for items that have already been looked up and saved in the local JSON cache
* Some items may not be available on the Trading Post
* Favourite item tracking is planned for a future version
* The project is currently contained in one Python file and may be refactored into separate modules later

## Planned Features

* Add a proper favourites.json feature for intentionally saved favourite items
* Allow users to view favourite items and fetch their current Trading Post prices
* Prevent duplicate favourite items
* Remove items from favourites
* Build a full item cache for searching all Guild Wars 2 item names
* Improve error handling with retry logic and logging
* Refactor the project into separate modules
* Eventually build a frontend version

## Future Goal

The long-term goal is to turn this into a small Guild Wars 2 item tracker where I can save frequently used items, view their current Trading Post prices, and eventually access everything through a simple frontend.
