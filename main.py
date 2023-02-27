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

    else:
        print('This game is cheaper on GOG. Here is the URL for the store page:', gogUrl)


if __name__ == '__main__':
    main()
