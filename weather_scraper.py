import requests
from bs4 import BeautifulSoup

def get_weather(city):
    url = f"https://www.weather-forecast.com/locations/{city}/forecasts/latest"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    weather = soup.find("span", class_="phrase").text
    return weather

if __name__ == "__main__":
    city = input("Enter city name: ").replace(" ", "-")
    weather = get_weather(city)
    print(f"The weather in {city.replace('-', ' ')} is: {weather}")
