import requests
import json

APIUrl = "https://api.steampowered.com/ISteamApps/GetAppList/v2/"
storeUrl = "https://store.steampowered.com//app/"


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
        if app["name"].lower() == appName:
            return app["appid"]
    notFound = "Item not found"
    return notFound


def getAppPrice(appID):
    appIDString = str(appID)
    response = requests.get(
        "http://store.steampowered.com/api/appdetails?appids=" + appIDString + "&cc=us&l=en")
    app = response.json()
    appDetails = app[str(appIDString)]
    appData = appDetails["data"]
    priceDetails = appData["price_overview"]
    appPrice = priceDetails["initial"]/100
    appPriceFormatted = priceDetails["final_formatted"]
    return appPrice, appPriceFormatted, storeUrl + str(appID)
