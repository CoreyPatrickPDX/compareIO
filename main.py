import webbrowser
import APIConnections.gogGameParse as gog
import APIConnections.steamGameParse as steam


def main():
    game = input("Please enter the game you wish to buy:")
    steamPrice, steamPriceFormatted, steamUrl = steam.returnPrice(game)
    gogPrice, gogPriceFormatted, gogUrl = gog.returnGamePrice(game)

    print("The price on Steam is:", steamPriceFormatted)
    print("The price on GOG is:", gogPriceFormatted)

    if (float(steamPrice) < float(gogPrice)):
        print(
            'This game is cheaper on Steam. Here is the URL for the store page:', steamUrl)
        bestPriceUrl = steamUrl

    else:
        print('This game is cheaper on GOG. Here is the URL for the store page:', gogUrl)
        bestPriceUrl = gogUrl

    while (True):
        try:
            openStore = str(input(
                'Would you like to open the store page for the lowest price? Please type Y for yes or N for no: '))
            while (openStore.lower() != 'y' and openStore.lower() != 'n'):
                openStore = input('Please enter Y for yes or N for no: ')

        except ValueError:
            print('Please enter Y for yes or N for no: ')
            continue

        else:
            break

    if (openStore.lower() == 'y'):
        webbrowser.open(bestPriceUrl, new=1)


if __name__ == '__main__':
    main()
