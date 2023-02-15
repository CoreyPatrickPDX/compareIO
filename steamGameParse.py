import requests
import json


def returnPrice(game):
    gameID = getAppID(game)
    gamePrice = getAppPrice(gameID)
    return (gamePrice)


def getAppID(appName):
    response = requests.get(
        "https://api.steampowered.com/ISteamApps/GetAppList/v2/")
    responseDict = response.json()
    appDict = responseDict["applist"]

    for app in appDict["apps"]:
        if app["name"] == appName:
            return app["appid"]


def getAppPrice(appID):
    appIDString = str(appID)
    response = requests.get(
        "http://store.steampowered.com/api/appdetails?appids=" + appIDString + "&cc=us&l=en")
    app = response.json()
    appDetails = app[str(appIDString)]
    appData = appDetails["data"]
    priceDetails = appData["price_overview"]
    appPrice = priceDetails["final_formatted"]
    return appPrice
