import requests
class WeatherClient:
    def __init__(self, API):
        self.API = API

    def get_moonphase(self, location):
        city = location
        format = 'json'

        # URL Components
        scheme = "http"
        host = "api.worldweatheronline.com"
        resource = "/premium/v1/weather.ashx"
        query = "key=%s&q=%s&format=%s&num_of_days=1" % (self.API,city,format)

        # Put it all together
        url = scheme + "://" + host + resource + "?" + query

        # Request library handles the *whole* protocol stack :)
        response = requests.get(url)
        data = response.json()


        # Show some interesting weather data
        current_moonphase = data['data']['weather'][0]['astronomy'][0]['moon_phase']
        return current_moonphase