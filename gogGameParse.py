import requests
import json


def main():
    game = "Fallout 2"
    print(getGamePrice(game))


def getGamePrice(game):
    response = requests.get(
        "https://embed.gog.com/games/ajax/filtered?search=" + game)
    # jprint(response.json())
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


# def jprint(obj):
#     text = json.dumps(obj, sort_keys=True, indent=4)
#     print(text)


if __name__ == '__main__':
    main()
