import PySimpleGUI as sg

from api.get_city_temperature import get_city_temperature
from db.create_log import create_log
from db.get_all_logs import get_all_logs
from models.eio.events import Events
from models.eio.inputs import Inputs
from models.eio.outputs import Outputs

sg.theme('DarkAmber')

layout = [
    [sg.Text('Current weather')],
    [sg.Text('City:'), sg.InputText(key=Inputs.CITY)],
    [sg.Button('Search', key=Events.SEARCH), sg.Button('Get logs', key=Events.GET_LOGS)],
    [sg.Text("", key=Outputs.TEMPERATURE), sg.Text("", key=Outputs.FEELS_LIKE)],
    [sg.Text("", key=Outputs.LOGS)]
]

def main():
    # Create the Window
    window = sg.Window('Window Title', layout)
    # Event Loop to process "events" and get the "values" of the inputs
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
            break

        if event == Events.SEARCH:
            temperature = get_city_temperature(values[Inputs.CITY])

            window[Outputs.TEMPERATURE].update(f"Temperature: {temperature.get('temp')}")
            window[Outputs.FEELS_LIKE].update(f"Feels like: {temperature.get('feels_like')}")

            create_log(values[Inputs.CITY], temperature.get("temp"))
        elif event == Events.GET_LOGS:
            logs = get_all_logs()
            formatted_logs = "\n".join([f"{log.payload}: {log.response} ℃ {log.created_at.strftime('%Y-%m-%d %H:%M:%S')}" for log in logs])
            window[Outputs.LOGS].update(formatted_logs)
    window.close()



if __name__ == "__main__":
    main()