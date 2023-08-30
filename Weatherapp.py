import tkinter as tk
import requests
import json
from tkinter import messagebox

def get_weather():
    api_key = "c91708293cfe0490deb03d3fdbd3868c"
    city = city_entry.get()
    url = f"http://api.weatherstack.com/current?access_key={api_key}&query={city}"
    resp = requests.get(url)
    try:
       if resp.status_code == 200:
        weather_data = json.loads(resp.text)
        temperature = weather_data["current"]["temperature"]
        humidity = weather_data["current"]["humidity"]
        description = weather_data["current"]["weather_descriptions"][0]
        
        result_message = (
            f"Current weather in {city}:\n"
            f"Temperature: {temperature}°C\n"
            f"Humidity: {humidity}%\n"
            f"Description: {description}"
        )
        messagebox.showinfo("Weather Information", result_message)
       else:
        messagebox.showerror("Invalid Entry", "Failed to fetch weather data.")
    except:
       messagebox.showerror("Invalid Entry", "Failed to fetch weather data.")    


m = tk.Tk()
m.title("Weather App")
m.geometry("300x100")

city_label = tk.Label(m, text="Enter the city:",font = ("Helvetica", 14))
city_label.pack()

city_entry = tk.Entry(m)
city_entry.pack()

calculate_button = tk.Button(m, text="GET", command=get_weather)
calculate_button.pack()


m.mainloop()

        
