# Air Quality (Ozone) in US

# ---------------------------------------------------
# Packages
from tkinter import *
import requests
import json


# ---------------------------------------------------
# Functions
def zipLookup():
    global myLabel
    myLabel.destroy()
    # Requests
    try:
        api_request = requests.get(
            'https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=' + str(zip.get()) + '&distance=25&API_KEY=A853FE86-136B-42EF-9E42-B3B2CEA1A2F1')
        api = json.loads(api_request.content)
        city = api[0]['ReportingArea']
        quality = api[0]['AQI']
        category = api[0]['Category']['Name']

        if category == 'Good':
            weather_color = '#0C0'
        elif category == 'Moderate':
            weather_color = '#FFFF00'
        elif category == 'Sensitive Groups':
            weather_color = '#ff9900'
        elif category == 'Unhealthy':
            weather_color = '#FF0000'
        elif category == 'Very Unhealthy':
            weather_color = '#990066'
        elif category == 'Hazardous':
            weather_color = '#660000'

        root.configure(background=weather_color)

        # Api[0] -> Ozone
        myLabel = Label(root, text=city + ', Air Quality ' + str(quality) + ' ' + category, \
                        font=('Helvetica', 16), background=weather_color)
        myLabel.grid(row=1, column=0, columnspan=2, padx=10)
    except Exception:
        e = 'No data'
        weather_color = 'lightgray'
        root.configure(background=weather_color)
        myLabel = Label(root, text=e, font=('Helvetica', 16), background=weather_color)
        myLabel.grid(row=1, column=0)


# ---------------------------------------------------
# GUI
root = Tk()
root.title('Air Quality: Ozone')
root.geometry('450x90')
root.resizable(False, False)


# ---------------------------------------------------
# Widgets
myLabel = Label(root)
zip = Entry(root)
zipButton = Button(root, text='Search Zipcode', command=zipLookup)


# ---------------------------------------------------
# Layouts
zip.grid(row=0, column=0, pady=10, padx=10, sticky=W+E+N+S)
zipButton.grid(row=0, column=1, pady=10, sticky=W+E+N+S)


# ---------------------------------------------------
# MainLoop
root.mainloop()
