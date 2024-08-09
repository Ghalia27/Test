import unittest
from utils.api_client import APIClient

API_KEY = 'all'
#para el API KEY pide ingresar tardeta de credito
client = APIClient(API_KEY)

class TestCountryAPI(unittest.TestCase):

    def test_get_valid_countries(self):
        country_codes = ['US', 'DE', 'GB']
        for code in country_codes:
            response = client.get(f'alpha/{code}')
            data=response.json()
            print(data)
            self.assertEqual(response.status_code, 200)
            data = response.json()
            self.assertEqual(data['alpha2Code'], code)

    def test_get_inexistent_countries(self):
        country_codes = ['ZZ', 'XX']
        for code in country_codes:
            response = client.get(f'alpha/{code}')
            self.assertEqual(response.status_code, 404)
            data = response.json()
            self.assertIn('error', data)

    def test_post_new_country(self):
        # Although POST is not available, simulate the request
        response = client.post('all', {
            "name": "Test Country",
            "alpha2_code": "TC",
            "alpha3_code": "TCY"
        })
        self.assertEqual(response.status_code, 405)  # Method Not Allowed for POST

if __name__ == '__main__':
    unittest.main()