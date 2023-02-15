import requests
import json


def main():
    game = "PUBG: BATTLEGROUNDS"
    gameID = getAppID(game)
    print(gameID)


def getAppID(appName):
    response = requests.get(
        "https://api.steampowered.com/ISteamApps/GetAppList/v2/")
    responseDict = response.json()

    appDict = responseDict["applist"]

    for app in appDict["apps"]:
        if app["name"] == appName:
            return app["appid"]


if __name__ == '__main__':
    main()
