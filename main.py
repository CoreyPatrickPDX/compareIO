import webbrowser
import PySimpleGUI as sg
import APIConnections.gogGameParse as gog
import APIConnections.steamGameParse as steam


def main():
    textTitle = sg.Text('Please enter game:', key="-OUT-",
                        font=('Arial Bold', 16), expand_x=True, justification='left')
    inputText = sg.Input('', enable_events=True, key='-INPUT-',
                         font=('Arial Bold', 16), expand_x=True, justification='left')
    searchButton = sg.Button('Search', key='-SEARCH-', font=('Arial Bold', 16))
    exitButton = sg.Button('Exit', font=('Arial Bold', 16))
    textGamePrice = sg.Text('Game Prices', key="-OUT-",
                            font=('Arial Bold', 20), expand_x=True, justification='center')
    steamText = sg.Text('Price on Steam:', key="-OUT-",
                        font=('Arial Bold', 16), justification='left')
    steamPriceText = sg.Text('', key="-STEAM PRICE-",
                             font=('Arial Bold', 16), justification='left')
    gogText = sg.Text('Price on GOG:', key="-OUT-",
                      font=('Arial Bold', 16), justification='left')
    gogPriceText = sg.Text('', key="-GOG PRICE-",
                           font=('Arial Bold', 16), justification='left')
    lowestURL = sg.Text('', key="-URL-",
                        font=('Arial Bold', 16), enable_events=True, justification='center')

    layout = [[textTitle, inputText],
              [searchButton],
              [textGamePrice],
              [steamText, steamPriceText],
              [gogText, gogPriceText],
              [lowestURL],
              [exitButton]]
    window = sg.Window("compareIO", layout)

    while True:
        event, values = window.read()
        print(event, values)
        if event == '-SEARCH-':
            game = values['-INPUT-']

            steamPrice, steamPriceFormatted, steamUrl = steam.returnPrice(
                game.lower())

            gogPrice, gogPriceFormatted, gogUrl = gog.returnGamePrice(
                game.lower())

            if (float(steamPrice) < float(gogPrice)):
                bestPriceUrl = steamUrl
                urlText = 'Click this text to go to Steam webpage.'
            else:
                bestPriceUrl = gogUrl
                urlText = 'Click this text to go to GOG webpage.'

            window['-STEAM PRICE-'].update(steamPriceFormatted)
            window['-GOG PRICE-'].update(gogPriceFormatted)
            window['-URL-'].update(urlText)
            window['-URL-'].set_cursor('hand2')
        if event == '-URL-':
            try:
                webbrowser.open(bestPriceUrl, new=1)
            except:
                return
        if event == 'Exit' or event == sg.WIN_CLOSED:
            break
    window.close()

    """ game = input("Please enter the game you wish to buy:").lower()
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
                'Would you like to open the store page for the lowest price? Please type Y for yes or N for no: ').lower())
            while (openStore != 'y' and openStore != 'n'):
                openStore = input('Please enter Y for yes or N for no: ')

        except ValueError:
            print('Please enter Y for yes or N for no')
            continue

        else:
            break

    if (openStore.lower() == 'y'):
        webbrowser.open(bestPriceUrl, new=1) """


if __name__ == '__main__':
    main()
