import pyowm
import requests
import datetime

class MyLocalWeather:
    def __init__(self,api_key) -> None:
        self.my_api_key = api_key
        self.my_owm = None
        self.my_ip = "None"
        self.my_city = "South Park"
        self.my_wdata = {}
        self.my_overview = "Hell"

    def create_owm(self):
        self.owm = pyowm.OWM( self.my_api_key ).weather_manager()
        
    def print_weather(self):
        ref_time = datetime.datetime.fromtimestamp( self.my_wdata.ref_time ).strftime('%Y-%m-%d %H:%M')
        print( f"Time\t\t: {  ref_time }" )
        print( f"Overview\t: { self.my_wdata.detailed_status}" )
        print( f"Wind Speed\t: { self.my_wdata.wind()}" )
        print( f"Humidity\t: { self.my_wdata.humidity}" )
        print( f"Temperature\t: { self.my_wdata.temperature('celsius')}" )
        print( f"Rain\t\t: { self.my_wdata.rain}" )
        print("\n")

    def get_current_weather(self):
        weather_api = self.owm.weather_at_place(self.my_city)  # give where you need to see the weather
        self.my_wdata = weather_api.weather                    # get out data in the mentioned location
        self.my_overview = weather_api.weather.detailed_status

    def get_ip(self):
        response = requests.get('https://api64.ipify.org?format=json').json()
        self.my_ip = response["ip"]

    def get_location(self):
        response = requests.get(f'https://ipapi.co/{self.my_ip}/json/').json()
        self.my_city = response.get("city")
        location_data = {
            "ip": self.my_ip,
            "city": self.my_city,
            "region": response.get("region"),
            "country": response.get("country_name")
        }
        print(location_data)