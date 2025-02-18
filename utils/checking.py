""" Methods for verifying API responses """

import json

class Checking:
    """ Check response status code """
    @staticmethod
    def check_status_code(result, expected_status):
        assert result.status_code == expected_status, f"❌ ERROR: Expected {expected_status}, but got {result.status_code}"
        print(f"✅ Status Code: {result.status_code} (Expected: {expected_status})")

    """ Check if response contains expected fields """
    @staticmethod
    def check_json_token(result, expected_fields):
        response_data = json.loads(result.text)
        assert list(response_data.keys()) == expected_fields, "❌ ERROR: Response fields do not match!"
        print(f"✅ JSON Fields Verified: {expected_fields}")

    """ Check if a field has an expected value """
    @staticmethod
    def check_json_value(result, field_name, expected_value):
        response_data = result.json()
        actual_value = response_data.get(field_name)
        assert actual_value == expected_value, f"❌ ERROR: Expected '{expected_value}' but got '{actual_value}'"
        print(f"✅ {field_name}: '{actual_value}' (Expected: '{expected_value}')")

    """ Check if a specific word exists in the field value """
    @staticmethod
    def check_json_search_word_in_value(result, field_name, search_word):
        response_data = result.json()
        field_value = response_data.get(field_name)
        assert search_word in field_value, f"❌ ERROR: '{search_word}' not found in '{field_value}'"
        print(f"✅ '{search_word}' found in {field_name}: '{field_value}'")
