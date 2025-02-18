import allure
from utils.checking import Checking
from utils.api import GoogleMapsAPI

@allure.epic("Google Maps API Tests")
class TestCreatePlace:
    @allure.description("Test for creating, updating, and deleting a new place")
    def test_create_new_place(self):
        print("\n=== Starting Google Maps API Test ===")

        # Create new place
        print("\n[STEP 1] Creating a new place...")
        result_post = GoogleMapsAPI.create_new_place()
        check_post = result_post.json()
        place_id = check_post.get("place_id")
        Checking.check_status_code(result_post, 200)
        Checking.check_json_token(result_post, ["status", "place_id", "scope", "reference", "id"])
        Checking.check_json_value(result_post, "status", "OK")
        print("✅ Place created successfully!")

        # Get created place
        print("\n[STEP 2] Retrieving created place...")
        result_get = GoogleMapsAPI.get_new_place(place_id)
        Checking.check_status_code(result_get, 200)
        Checking.check_json_token(result_get,
            ["location", "accuracy", "name", "phone_number", "address", "types", "website", "language"])
        Checking.check_json_value(result_get, "address", "29, side layout, cohen 09")
        print("✅ Place retrieved successfully!")

        # Update place
        print("\n[STEP 3] Updating place address...")
        result_put = GoogleMapsAPI.put_new_place(place_id)
        Checking.check_status_code(result_put, 200)
        Checking.check_json_token(result_put, ["msg"])
        Checking.check_json_value(result_put, "msg", "Address successfully updated")
        print("✅ Place updated successfully!")

        # Get updated place
        print("\n[STEP 4] Verifying updated address...")
        result_get = GoogleMapsAPI.get_new_place(place_id)
        Checking.check_status_code(result_get, 200)
        Checking.check_json_value(result_get, "address", "100 Lenina street, RU")
        print("✅ Address updated successfully!")

        # Delete place
        print("\n[STEP 5] Deleting place...")
        result_delete = GoogleMapsAPI.delete_new_place(place_id)
        Checking.check_status_code(result_delete, 200)
        Checking.check_json_token(result_delete, ["status"])
        Checking.check_json_value(result_delete, "status", "OK")
        print("✅ Place deleted successfully!")

        # Verify deletion
        print("\n[STEP 6] Confirming place deletion...")
        result_get = GoogleMapsAPI.get_new_place(place_id)
        Checking.check_status_code(result_get, 404)
        Checking.check_json_token(result_get, ["msg"])
        Checking.check_json_search_word_in_value(result_get, "msg", "operation failed")
        print("✅ Deletion confirmed!")

        print("\n=== Google Maps API Test Completed Successfully ===")
