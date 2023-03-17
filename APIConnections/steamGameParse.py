import requests
import json

APIUrl = "https://api.steampowered.com/ISteamApps/GetAppList/v2/"
storeUrl = "https://store.steampowered.com//app/"


def apiRequest(url):
    return requests.get(url)


def returnPrice(game):
    gameID = getAppID(game)
    gamePrice = getAppPrice(gameID)
    return (gamePrice)


def getAppID(appName):
    try:
        response = apiRequest(
            "https://api.steampowered.com/ISteamApps/GetAppList/v2/")
    except requests.exceptions.HTTPError as errh:
        print("Http Error:", errh)
    except requests.exceptions.ConnectionError as errc:
        print("Error Connecting:", errc)
    except requests.exceptions.Timeout as errt:
        print("Timeout Error:", errt)
    except requests.exceptions.RequestException as err:
        print("OOps: Something Else", err)

    responseDict = response.json()
    appDict = responseDict["applist"]

    for app in appDict["apps"]:
        if app["name"].lower() == appName:
            return app["appid"]
    notFound = "Item not found"
    return notFound


def getAppPrice(appID):
    appIDString = str(appID)
    response = apiRequest(
        "http://store.steampowered.com/api/appdetails?appids=" + appIDString + "&cc=us&l=en")

    app = response.json()
    appDetails = app[str(appIDString)]
    appData = appDetails["data"]
    priceDetails = appData["price_overview"]
    appPrice = priceDetails["final"]/100
    appPriceFormatted = priceDetails["final_formatted"]
    return appPrice, appPriceFormatted, storeUrl + str(appID)
