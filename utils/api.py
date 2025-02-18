from utils.http_methods import Http_methods

""" Methods for interacting with Google Maps API """

BASE_URL = "https://rahulshettyacademy.com"
API_KEY = "?key=qaclick123"

class GoogleMapsAPI:
    """ Create a new place """
    @staticmethod
    def create_new_place():
        json_data = {
            "location": {"lat": -38.383494, "lng": 33.427362},
            "accuracy": 50,
            "name": "Frontline house",
            "phone_number": "(+91) 983 893 3937",
            "address": "29, side layout, cohen 09",
            "types": ["shoe park", "shop"],
            "website": "http://google.com",
            "language": "French-IN"
        }

        url = f"{BASE_URL}/maps/api/place/add/json{API_KEY}"
        print(f"[API REQUEST] POST: {url}")
        result = Http_methods.post(url, json_data)
        return result

    """ Get place details """
    @staticmethod
    def get_new_place(place_id):
        url = f"{BASE_URL}/maps/api/place/get/json{API_KEY}&place_id={place_id}"
        print(f"[API REQUEST] GET: {url}")
        result = Http_methods.get(url)
        return result

    """ Update place details """
    @staticmethod
    def put_new_place(place_id):
        url = f"{BASE_URL}/maps/api/place/update/json{API_KEY}"
        json_data = {"place_id": place_id, "address": "100 Lenina street, RU", "key": "qaclick123"}

        print(f"[API REQUEST] PUT: {url}")
        result = Http_methods.put(url, json_data)
        return result

    """ Delete a place """
    @staticmethod
    def delete_new_place(place_id):
        url = f"{BASE_URL}/maps/api/place/delete/json{API_KEY}"
        json_data = {"place_id": place_id}

        print(f"[API REQUEST] DELETE: {url}")
        result = Http_methods.delete(url, json_data)
        return result
