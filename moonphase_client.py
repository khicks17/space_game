import requests
class WeatherClient:
    def __init__(self, API):
        self.API = API

    def get_moonphase(self, location):
        city = location
        format = 'json'



        # URL Components
        scheme = "https"
        host = "api.worldweatheronline.com"
        resource = "api.worldweatheronline.com/premium/v1/weather.ashx"
        query = "key=%s&q=%s&format=%s" % (self.API,city,format)

        # Put it all together
        url = scheme + "://" + host + resource + "?" + query

        # Request library handles the *whole* protocol stack :)
        r = requests.get(url)
        data = r.json()

        # Show some interesting weather data
        current_moonphase = data['weather']['moon_phase']
        return current_moonphase