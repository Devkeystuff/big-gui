import PySimpleGUI as sg
import requests

from models.inputs import Inputs

sg.theme('DarkAmber')

layout = [  [sg.Text('Current weather')],
            [sg.Text('City:'), sg.InputText(key=Inputs.CITY)],
            [sg.Button('Ok'), sg.Button('Cancel')] ]

def get_city(name: str) -> str:
    try:
        city = requests.get("")
    except:
        # TODO: show error in GUI
        print("Couldn't fetch city")

def main():
    # Create the Window
    window = sg.Window('Window Title', layout)
    # Event Loop to process "events" and get the "values" of the inputs
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
            break

        if Inputs.CITY in event:
            city = get_city()
    window.close()



if __name__ == "__main__":
    main()