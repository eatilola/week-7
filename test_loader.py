import unittest
import pandas as pd
from loader import *

class TestLoader(unittest.TestCase):
    def test_valid_locations(self):
        geolocator = get_geolocator()
        result = fetch_location_data(geolocator, "Museum of Modern Art")
        self.assertIsNotNone(result, "A valid location should return geolocation data.")

        self.assertIsInstance(result, dict, "The result should be a dictionary.")

        self.assertIn("latitude", result, "The result should contain 'latitude'.")
        self.assertIn("longitude", result, "The result should contain 'longitude'.")
        self.assertIn("address", result, "The result should contain 'address'.")
        
        self.assertAlmostEqual(result["latitude"], 40.7618552, places=2, 
                          msg="Museum of Modern Art latitude should be approximately 40.76")
        self.assertAlmostEqual(result["longitude"], -73.9782438, places=2,
                            msg="Museum of Modern Art longitude should be approximately -73.98")
        
        # Test USS Alabama Battleship Memorial Park
        result2 = fetch_location_data(geolocator, "USS Alabama Battleship Memorial Park")
        self.assertIsNotNone(result2, "A valid location should return geolocation data.")
        self.assertIsInstance(result2, dict, "The result should be a dictionary.")
        self.assertIn("latitude", result2, "The result should contain 'latitude'.")
        self.assertIn("longitude", result2, "The result should contain 'longitude'.")
        self.assertIn("address", result2, "The result should contain 'address'.")
        
        self.assertAlmostEqual(result2["latitude"], 30.684373, places=2,
                            msg="USS Alabama latitude should be approximately 30.68")
        self.assertAlmostEqual(result2["longitude"], -88.015316, places=2,
                            msg="USS Alabama longitude should be approximately -88.02")


    def test_invalid_location(self):
        geolocator = get_geolocator()
        result = fetch_location_data(geolocator, "asdfqwer1234")

        
        self.assertIsNotNone(result, "Invalid location should still return a dictionary.")
        self.assertEqual(result["location"], "asdfqwer1234")
        self.assertTrue(pd.isna(result["latitude"]), "Latitude should be NaN for invalid location.")
        self.assertTrue(pd.isna(result["longitude"]), "Longitude should be NaN for invalid location.")
        self.assertTrue(pd.isna(result["address"]), "Address should be NaN for invalid location.")

if __name__ == "__main__":
    unittest.main()
