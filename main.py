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


if __name__ == '__main__':
    main()
