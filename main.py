import APIConnections.gogGameParse as gog
import APIConnections.steamGameParse as steam


def main():
    game = input("Please enter the game you wish to buy:")
    steamPrice = steam.returnPrice(game)
    gogPrice = gog.returnGamePrice(game)

    print("The price on Steam is:", steamPrice)
    print("The price on GOG is:", gogPrice)


if __name__ == '__main__':
    main()
