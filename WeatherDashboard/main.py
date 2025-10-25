import requests


API_KEY = "80e87c3265adc448bf375a6a5f7db73b"


def main():
    lat = "60.7212"
    lon = "-135.0568"
    units = "metric"
    url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_KEY}&units={units}"
    response = requests.get(url)
    data = response.json()
    print(f"Today: {data["main"]["temp"]}°C")


if __name__ == "__main__":
    main()