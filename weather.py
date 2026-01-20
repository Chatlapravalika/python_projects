import requests

API_KEY = "PASTE_YOUR_API_KEY_HERE"   # <-- Put your API key here
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

def get_weather(city):
    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"   # Celsius
    }

    response = requests.get(BASE_URL, params=params)
    data = response.json()

    if data["cod"] != 200:
        print("❌ City not found!")
        return

    city_name = data["name"]
    temp = data["main"]["temp"]
    humidity = data["main"]["humidity"]
    weather = data["weather"][0]["description"]
    wind_speed = data["wind"]["speed"]

    print("\n🌍 Weather Report")
    print("----------------------")
    print(f"City: {city_name}")
    print(f"Temperature: {temp} °C")
    print(f"Condition: {weather}")
    print(f"Humidity: {humidity}%")
    print(f"Wind Speed: {wind_speed} m/s")

if __name__ == "__main__":
    print("=== Weather App ===")
    city = input("Enter city name: ")
    get_weather(city)
