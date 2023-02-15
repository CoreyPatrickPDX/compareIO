import requests
import json


def main():
    game = "Monster Sanctuary"
    gameID = getAppID(game)
    getAppPrice(gameID)


def getAppID(appName):
    response = requests.get(
        "https://api.steampowered.com/ISteamApps/GetAppList/v2/")
    responseDict = response.json()

    appDict = responseDict["applist"]

    for app in appDict["apps"]:
        if app["name"] == appName:
            return app["appid"]


def getAppPrice(appID):
    response = requests.get(
        "http://store.steampowered.com/api/appdetails?appids=" + str(appID) + "&cc=us&l=en")
    # jprint(response.json())
    appIDString = str(appID)
    app = response.json()
    appDetails = app[str(appIDString)]
    appData = appDetails["data"]
    priceDetails = appData["price_overview"]
    appPrice = priceDetails["final_formatted"]
    print(type(appPrice))


if __name__ == '__main__':
    main()
