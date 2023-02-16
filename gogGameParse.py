import requests
import json


def returnGamePrice(game):
    response = requests.get(
        "https://embed.gog.com/games/ajax/filtered?search=" + game)
    gameJson = response.json()
    gameList = gameJson["products"]
    for item in gameList:
        if game == item["title"]:
            gamePriceInfo = item["price"]
            gamePrice = gamePriceInfo["symbol"] + gamePriceInfo["amount"]
            return gamePrice
    else:
        notFound = "Item not found"
        reuturn = notFound
