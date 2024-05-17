import requests


API_KEY = "ad7d87dbaad77836591d61cca49b026d"


def get_data(location, forecast_days=2, type=None):
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={location}&appid={API_KEY}"
    response = requests.get(url)
    data = response.json()
    filtered_data = data["list"]
    nr_values = 8 * forecast_days
    filtered_data = filtered_data[:nr_values]
    if type=="Temperature":
        filtered_data = [dict["main"]["temp"] for dict in filtered_data]
    if type=="Sky":
        filtered_data = [dict["weather"]["main"] for dict in filtered_data]
    return filtered_data


if __name__=="__main__":
    print(get_data(location="Tokyo"))