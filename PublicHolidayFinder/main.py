import requests


def main():
    year = "2025"
    country_code = "CA"
    url = f"https://date.nager.at/api/v3/publicholidays/{year}/{country_code}"
    public_holidays = requests.get(url).json()
    for holiday in public_holidays:
        print(f"{holiday['date']}: {holiday['localName']}")


if __name__ == "__main__":
    main()