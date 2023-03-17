import unittest
from apiRequest import apiRequest
from APIConnections.steamGameParse import returnPrice
from APIConnections.gogGameParse import returnGamePrice


class TestAPIRequest(unittest.TestCase):
    def test_apiRequest(self):
        self.assertEqual(apiRequest(
            'https://api.steampowered.com/ISteamApps/GetAppList/v2/').status_code, 200)
        self.assertEqual(apiRequest(
            'http://store.steampowered.com/api/appdetails?appids=526870&cc=us&l=en').status_code, 200)
        self.assertEqual(apiRequest(
            "https://embed.gog.com/games/ajax/filtered?search=cyberpunk_2077").status_code, 200)

    def test_not_apiRequest(self):
        self.assertEqual(apiRequest(
            'https://api.steamowered.com/ISteamApps/GetAppList/v2/'), 'Error Connecting')
        self.assertEqual(apiRequest(
            'https://api.steamowered.com/ISteamApps/GetAppList/v2/'), 'Error Connecting')


if __name__ == '__main__':
    unittest.main()
