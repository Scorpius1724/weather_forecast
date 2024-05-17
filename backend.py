import requests


API_KEY = "ad7d87dbaad77836591d61cca49b026d"


def get_data(location, forecast_days=None, type=None):
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={location}&appid={API_KEY}"
    response = requests.get(url)
    data = response.json()
    return data


if __name__=="__main__":
    print(get_data(location="Tokyo"))