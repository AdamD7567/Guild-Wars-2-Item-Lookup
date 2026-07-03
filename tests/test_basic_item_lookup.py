import json

from basic_item_lookup import format_coins, validate_input, find_item_in_cache, add_item_to_cache

# -------------------------------------------------
# Coin Formatting tests for different input values
# -------------------------------------------------
def test_format_coins_zero():
    assert format_coins(0) == "0g 0s 0c"

def test_format_coins_copper_only():
    assert format_coins(99) == "0g 0s 99c"

def test_format_coins_silver_and_copper():
    assert format_coins(150) == "0g 1s 50c"

def test_format_coins_gold_silver_and_copper():
    assert format_coins(12345) == "1g 23s 45c"


# -------------------------------------------------
# Validation tests for item lookup by ID
# -------------------------------------------------
def test_validate_input_accepts_numeric_string():
    assert validate_input("19721") is True

def test_validate_input_rejects_text():
    assert validate_input("ectoplasm") is False


# -------------------------------------------------
# Tests for looking up items within the established cache
# -------------------------------------------------
def test_find_item_in_cache_returns_none_when_file_missing(tmp_path):
    file_path = tmp_path / "looked_up_items.json"
    
    assert find_item_in_cache("Blueberry", file_path) is None

# -------------------------------------------------
# Tests for adding items to the cache / creating the cache
# -------------------------------------------------
def test_add_item_to_cache_adds_item(tmp_path):
    file_path = tmp_path / "looked_up_items.json"

    item_data = {
        "id": 19222,
        "name": "Test Data"
    }

    add_item_to_cache(item_data, file_path)

    with open(file_path, "r", encoding="utf-8") as read_file:
        saved_items = json.load(read_file)

    assert saved_items == [
        {
            "id": 19222,
            "name": "Test Data"
        }
    ]