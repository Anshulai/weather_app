import requests
from tkinter import *

api_key = '30d4741c779ba94c470ca1f63045390a'

def get_weather():
    user_input = city_name.get()
    weather_data = requests.get(
        f"https://api.openweathermap.org/data/2.5/weather?q={user_input}&units=imperial&APPID={api_key}")

    if weather_data.json()['cod'] == '404':
        weather.set("No City Found")
        temp.set("")
    else:
        weather.set(weather_data.json()['weather'][0]['main'])
        temp_f = round(weather_data.json()['main']['temp'])
        temp_c = round((temp_f - 32) * 5/9) 
        temp.set(f"{temp_c}ºC")  

root = Tk()
root.title("Weather App")
root.geometry("300x200")
root.configure(bg='light blue')

city_name = StringVar()
weather = StringVar()
temp = StringVar()

Label(root, text = "City Name", font=('Helvetica', 15, 'bold'), bg='light blue').grid(row = 0, sticky = W)
Entry(root, textvariable = city_name, font=('Helvetica', 12)).grid(row = 0, column = 1)

Button(root, text = "Get Weather", command = get_weather, bg='blue', fg='white', font=('Helvetica', 12, 'bold')).grid(row = 0, column = 2)

Label(root, textvariable = weather, font=('Helvetica', 15, 'bold'), bg='light blue').grid(row = 1, column = 0)
Label(root, textvariable = temp, font=('Helvetica', 15, 'bold'), bg='light blue').grid(row = 1, column = 1)

root.mainloop()