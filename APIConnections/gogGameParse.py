import requests
import json
from apiRequest import apiRequest

APIUrl = "https://embed.gog.com/games/ajax/filtered?search="
storeUrl = "https://www.gog.com/"


def returnGamePrice(game):
    response = apiRequest(
        APIUrl + game)

    gameJson = response.json()
    gameList = gameJson["products"]
    for item in gameList:
        if game == item["title"].lower():
            gamePriceInfo = item["price"]
            gamePrice = gamePriceInfo["amount"]
            gamePriceFormatted = gamePriceInfo["symbol"] + gamePrice
            gogUrl = storeUrl + str(item["url"])
            return gamePrice, gamePriceFormatted, gogUrl
    else:
        notFound = "Item not found"
        return notFound
