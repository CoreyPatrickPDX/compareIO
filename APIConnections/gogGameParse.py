import requests
import json

APIUrl = "https://embed.gog.com/games/ajax/filtered?search="
storeUrl = "gog.com"


def returnGamePrice(game):
    response = requests.get(
        APIUrl + game)
    gameJson = response.json()
    gameList = gameJson["products"]
    for item in gameList:
        if game.lower() == item["title"].lower():
            gamePriceInfo = item["price"]
            gamePrice = gamePriceInfo["amount"]
            gamePriceFormatted = gamePriceInfo["symbol"] + gamePrice
            gogUrl = storeUrl + str(item["url"])
            return gamePrice, gamePriceFormatted, gogUrl
    else:
        notFound = "Item not found"
        return notFound
